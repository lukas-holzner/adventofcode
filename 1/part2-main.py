with open('1/input.txt') as f:
    lines = f.readlines()

elves = [(1,0)]

for l in lines:
    line = l.rstrip('\n')
    if line == '':
        elves.append((len(elves)+1,0))
    else:
        i = len(elves)-1
        sum = elves[i][1] + int(line)
        elves[i] = (i+1 ,sum)

topthree = sorted(elves, key=lambda x:x[1])[-3:]
print("Top three: "+ str(topthree))

sum = 0
for i in topthree:
    sum += i[1]

print("\n Sum: " + str(sum))
# test