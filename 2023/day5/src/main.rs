use std::fs::File;
use std::io::prelude::*;
use std::str::FromStr;
use std::collections::HashMap;
use rayon::prelude::*;
use regex::Regex;
use indicatif::ProgressBar;

fn get_seed_location(seed: i64, mappings: &HashMap<String, Vec<(i64, i64, i64)>>) -> i64 {
    let mut value = seed;
    let categories = vec!["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"];
    for category in categories {
        for rule in &mappings[category] {
            let (dest_start, src_start, length) = rule;
            if *src_start <= value && value < *src_start + *length {
                value = *dest_start + (value - *src_start);
                break;
            }
        }
    }
    value
}

fn process_seed_range(start: i64, end: i64, mappings: &HashMap<String, Vec<(i64, i64, i64)>>) -> i64 {
    let pb = ProgressBar::new((end - start) as u64);
    let mut lowest_location = i64::MAX;
    for j in start..end {
        pb.inc(1);
        lowest_location = lowest_location.min(get_seed_location(j, mappings));
    }
    pb.finish();
    lowest_location
}

fn interpret_almanac(almanac: &str) -> i64 {
    let lines: Vec<&str> = almanac.lines().collect();
    let re = Regex::new(r"\d+").unwrap();
    let seeds: Vec<i64> = re.find_iter(lines[0])
        .map(|m| i64::from_str(m.as_str()).unwrap())
        .collect();
    let mut mappings: HashMap<String, Vec<(i64, i64, i64)>> = HashMap::new();
    let mut current_map = String::new();

    for line in &lines[1..] {
        if line.contains("map:") {
            current_map = line.split_whitespace().next().unwrap().to_string();
            mappings.insert(current_map.clone(), vec![]);
        } else if !line.is_empty() {
            let values: Vec<i64> = re.find_iter(line)
                .map(|m| i64::from_str(m.as_str()).unwrap())
                .collect();
            mappings.get_mut(&current_map).unwrap().push((values[0], values[1], values[2]));
        }
    }

    let lowest_location = seeds.par_chunks(2)
        .map(|chunk| process_seed_range(chunk[0], chunk[0] + chunk[1], &mappings))
        .min()
        .unwrap();

    lowest_location
}

fn main() {
    let mut file = File::open("/workspaces/adventofcode/2023/day5/input.txt").unwrap();
    let mut almanac = String::new();
    file.read_to_string(&mut almanac).unwrap();
    let lowest = interpret_almanac(&almanac);
    println!("Location {} is the lowest location.", lowest);
}