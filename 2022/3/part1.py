

with open('3/input.txt') as f:
    lines = f.readlines()

total = 0
for l in lines:
    line = l.rstrip('\n')
    firstpart = line[:int(len(line)/2)]
    secondpart = line[int(len(line)/2):]
    for i in set(firstpart):
        if i in secondpart:
            if ord(i) < 91:
                total += ord(i)-38 # -38 to convert ASCII uppercase to score
            else:
                total += ord(i)-96 # -96 to convert ASCII lowercase to score

print("The total score is: {}".format(total))