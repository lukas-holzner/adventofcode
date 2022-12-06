line = open('6/input.txt').readline().strip()
for i in range(len(line)):
    if len(set(line[i:(i+4)])) == 4:
        exit("Line {} with {}".format(i+4,line[i:i+4]))