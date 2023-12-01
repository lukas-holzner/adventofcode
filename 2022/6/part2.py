line = open('6/input.txt').readline().strip()
for i in range(len(line)):
    if len(set(line[i:(i+14)])) == 14:
        exit("Line {} with {}".format(i+14,line[i:i+14]))