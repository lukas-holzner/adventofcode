#!/usr/bin/env python3

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
    
    seed_lowest=0

    seed_locations = {}

    for seed in seeds:
        seed_locations[str(seed)] = {}
        value = seed
        for category in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            for rule in mappings[category]:
                dest_start, src_start, length = rule
                if src_start <= value < src_start + length:
                    value = dest_start + (value - src_start)
                    seed_locations[str(seed)][category] = value
                    break
            else:
                value = value
                seed_locations[str(seed)][category] = value
        if value < lowest_location:
            seed_lowest = seed
            lowest_location = value

    return seed_locations[str(seed_lowest)]

with open('2023/5/input.txt') as f:
    almanac = f.read()
    seed_journey = interpret_almanac(almanac)
    print(seed_journey)

    print(f"Seed {seed_journey['humidity-to-location']} is the lowest location.")