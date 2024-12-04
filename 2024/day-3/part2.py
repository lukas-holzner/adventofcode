#!/usr/bin/env python3
import re
sum_mult = 0
with open("day-3/data.txt", "r") as file:
    do_mult = True
    inp = file.read().replace("\n", "")
    matchlist = list(re.finditer(r"(?P<do>do\(\))|(?P<dont>don't\(\))|(?P<mul>mul\((\d?\d?\d),(\d?\d?\d)\))",inp))
    for match in matchlist:
        grouptype = [name for name, value in match.groupdict().items() if value is not None][0]
        match grouptype:
            case "mul":
                if do_mult:
                  sum_mult += int(match.groups()[3]) * int(match.groups()[4])
            case "do":
                do_mult = True
            case "dont":
                do_mult = False
            case _:
                exit(1)

print(sum_mult)