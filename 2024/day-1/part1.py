#!/usr/bin/python3

import re

leftlist = []
rightlist = []

with open("data.txt", "r") as f:
    for line in f.readlines():
        left,right = re.split(r'\D+', line.replace("\n",""), maxsplit=2)
        leftlist.append(int(left))
        rightlist.append(int(right))

rightlist.sort()
leftlist.sort()

score = 0

for i in range(0,len(rightlist)):
    score += abs(rightlist[i]-leftlist[i])

print(score)