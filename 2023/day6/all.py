import math


# -x^2+x*t = d
# x^2 - x*t + d = 0
# x = (t +- sqrt(t^2 - 4*d))/2

def get_winning_distance_range(time, distance):
    fromc = 0.5*(time - (time**2 - 4*distance)**0.5)
    toc = 0.5*(time + (time**2 - 4*distance)**0.5)
    print(fromc,toc)
    if toc - math.floor(toc) == 0.0:
        toc -= 1.0
    if fromc - math.floor(fromc) == 0.0:
        fromc += 1.0
    return (
            math.ceil(fromc),
            math.floor(toc)
        )

def parse_paper_part1(paper):
    lines = paper.split('\n') 
    time = list(map(int,lines[0].split(': ')[1].split()))
    distance = list(map(int,lines[1].split(': ')[1].split()))

    return list(zip(time,distance))

def parse_paper_part2(paper):
    lines = paper.split('\n') 
    time = int(''.join(lines[0].split(': ')[1].split()))
    distance = int(''.join(lines[1].split(': ')[1].split()))
    return [(time,distance)]

def calculate_total_winning_ms(timetodist):
    total = 1
    print(timetodist)
    for time, distance in timetodist:
        fromc,toc = get_winning_distance_range(time, distance)
        winning_ms = (toc - fromc + 1)
        print(f"Time: {time}, Distance: {distance}, Number of Winning ms: {winning_ms}, From: {fromc}, To: {toc}")
        total *= winning_ms
    return total

with open("/workspaces/adventofcode/2023/day6/input.txt") as f:
    paper = f.read()
    timetodist = parse_paper_part1(paper)
    print(f"Part1 Total Winning Milliseconds: {calculate_total_winning_ms(timetodist)}")
    timetodist = parse_paper_part2(paper)
    print(f"Part2 Total Winning Milliseconds: {calculate_total_winning_ms(timetodist)}")

    