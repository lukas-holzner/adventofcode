#! /usr/bin/env python3
safe_report = 0


with open("day-2/data.txt", "r") as file:
    for line in file:
        report = list(map(int, line[:-1].split(" ")))
        sign = 1 if report[0] - report[1] > 0 else -1
        issafe = 1
        for i in range(0,len(report)-1):
            if not(0 < (report[i]-report[i+1])*sign < 4):
                issafe = 0
                break
        safe_report += issafe

print(safe_report)
        