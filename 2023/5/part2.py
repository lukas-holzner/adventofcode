#!/usr/bin/env python3

from tqdm import tqdm

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

    for i in range(0, len(seeds), 2):
        print(f"Processing seeds {seeds[i]} to {seeds[i]+seeds[i+1]}")
        for j in tqdm(range(seeds[i], seeds[i]+seeds[i+1])):
            lowest_location = min(lowest_location, get_seed_location(j, mappings))

    return lowest_location

with open('2023/5/test.txt') as f:
    almanac = f.read()
    lowest = interpret_almanac(almanac)

    print(f"Location {lowest} is the lowest location.")