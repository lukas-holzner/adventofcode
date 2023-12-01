with open('1/input.txt') as f:
    lines = f.readlines()

elves = [0]

for l in lines:
    line = l.rstrip('\n')
    if line == '':
        elves.append(0)
    else:
        elves[len(elves)-1] += int(line)

bestelv = (-1,0)
for idx,elv in enumerate(elves):
    print("Elv {} with {} calories".format(idx+1, elv))
    if elv > bestelv[1]:
        bestelv = (idx, elv)

print("The best Elv is : \n\n")
print("Elv {} with {} calories".format(bestelv[0]+1, bestelv[1]))