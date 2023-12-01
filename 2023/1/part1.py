#!/usr/bin/python
totalsum = 0

with open('2023/1/input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip('\n')
    number=""
    for ch in line:
        if ch in "0123456789":
            number += ch
            break
    
    for ch in line[::-1]:
        if ch in "0123456789":
            number += ch
            break
    
    print(number)
    totalsum += int(number)

print(f'Total sum is {totalsum}')
        

