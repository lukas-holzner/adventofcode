#!/usr/bin/env python3
import re
with open("day-3/data.txt", "r") as file:
    inp = file.read().replace("\n", "")
    sum_of_mult = sum(list(map(lambda x: int(x[0])*int(x[1]), re.findall(r"mul\((\d?\d?\d),(\d?\d?\d)\)",inp))))
    print(sum_of_mult)