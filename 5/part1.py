from parse import *

stacks = {
    "1": ['T','D','W','Z','V','P'],
    "2": ['L','S','W','V','F','J','D'],
    "3": ['Z','M','L','S','V','T','B','H'],
    "4": ['R','S','J'],
    "5": ['C','Z','B','G','F','M','L','W'],
    "6": ['Q','W','V','H','Z','R','G','B'],
    "7": ['V','J','P','C','B','D','N'],
    "8": ['P','T','B','Q'],
    "9": ['H','G','Z','R','C'],
}

pattern = "move {} from {} to {}"

def move_crates(num, mv_from, mv_to):
    global stacks
    buffer =  []
    for i in range(int(num)):
        buffer.append(stacks[mv_from].pop())
    print("\nmove {} from {} to {}".format(num,mv_from,mv_to))
    print("Buffer: {}".format(buffer))
    stacks[mv_to].extend(buffer)

with open('5/input.txt') as f:
    lines = list(map(str.strip ,f.readlines()))

for line in lines:
    r = parse(pattern, line)
    move_crates(r[0], r[1], r[2])

result = ""
for i in range(1,10):
    print("\n\nStack: {} has {}".format(i, stacks[str(i)]))
    result += stacks[str(i)].pop()

print("\n\n The RESULT is: {}".format(result))