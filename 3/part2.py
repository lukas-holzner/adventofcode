def findbatch(elvgroup):
    for c in elvgroup[0]:
        if c in elvgroup[1] and c in elvgroup[2]:
            return c
    raise Exception('No Batch found in Elvgroup')

with open('3/input.txt') as f:
    lines = list(map(str.strip ,f.readlines()))

total = 0

for i in range(0,len(lines),3):
    print("Elv Group Nr. {}".format(int(i/3)+1))
    elvgroup = lines[i:i+3]
    batch = findbatch(elvgroup)
    print("\t Batch is {}".format(batch))
    if ord(batch) < 91:
        total += ord(batch)-38 # -38 to convert ASCII uppercase to score
    else:
        total += ord(batch)-96 # -96 to convert ASCII lowercase to score


print("\n\nThe total score is: {}".format(total))

