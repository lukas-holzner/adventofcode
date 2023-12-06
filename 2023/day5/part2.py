#!/usr/bin/env python3

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def get_seed_location(seed, mappings):
    value = seed
    for category in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        for rule in mappings[category]:
            dest_start, src_start, length = rule
            if src_start <= value < src_start + length:
                value = dest_start + (value - src_start)
                break
        else:
            value = value
    return value

def process_seed_range(start, end, mappings):
    lowest_location = float('inf')
    for j in tqdm(range(start, start+end)):
        lowest_location = min(lowest_location, get_seed_location(j, mappings))
    return lowest_location

def interpret_almanac(almanac):
    lines = almanac.split('\n')
    seeds = list(map(int, lines[0].split(': ')[1].split()))
    mappings = {}
    current_map = None

    for line in lines[1:]:
        if 'map:' in line:
            current_map = line.split(' ')[0]
            mappings[current_map] = []
        elif line:
            mappings[current_map].append(list(map(int, line.split())))

    lowest_location = float('inf')

    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(0, len(seeds), 2):
            print(f"Processing seeds {seeds[i]} to {seeds[i]+seeds[i+1]}")
            futures.append(executor.submit(process_seed_range, seeds[i], seeds[i+1], mappings))

        lowest_location = min(f.result() for f in futures)

    return lowest_location

with open('2023/5/input.txt') as f:
    almanac = f.read()
    lowest = interpret_almanac(almanac)

    print(f"Location {lowest} is the lowest location.")