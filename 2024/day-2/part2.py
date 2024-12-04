#! /usr/bin/env python3

# The lazy brute force method xD

safe_report = 0

def isSafe(report, sign):
    for i in range(0,len(report)-1):
        if not(0 < (report[i]-report[i+1])*sign < 4):
            return False
    return True

with open("day-2/data.txt", "r") as file:
    for line in file:
        report = list(map(int, line[:-1].split(" ")))
        sign = 1 if report[0] - report[1] > 0 else -1
        issafe = 0
        if isSafe(report, sign):
            issafe = 1
        else:
            for i in range(len(report)):
                rep = [report[j] for j in range(len(report)) if j != i]
                sign = 1 if rep[0] - rep[1] > 0 else -1
                if isSafe(rep, sign):
                    issafe = 1
                    print(f"{line} safed with removing {report[i]} at the index {i}")
                    break
        safe_report += issafe

print(safe_report)
        