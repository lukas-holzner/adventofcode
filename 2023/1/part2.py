#!/usr/bin/python
totalsum = 0

def reversestring(word: str):
    return word[::-1]

def getfirstnumber(written, line):
    word=""
    for ch in line:
        if ch in "123456789":
            return ch
        word += ch
        stoploop = False
        for idx, item in enumerate(written):
            if item in word:
                return str(idx+1)
    raise Exception

writtennumbers= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
writtennumbersreverse = list(map(reversestring, writtennumbers))

with open('2023/1/input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip('\n')
    number=""
    number += str(getfirstnumber(writtennumbers, line))
    number += str(getfirstnumber(writtennumbersreverse, reversestring(line)))   
    
    print(number)
    totalsum += int(number)

print(f'Total sum is {totalsum}')
        

