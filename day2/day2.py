f = open('day2.txt', 'r')
numValid = 0
for line in f:
    lineList = line.split(" ")
    lowHighVals = lineList[0].split("-")
    low = int(lowHighVals[0])
    high = int(lowHighVals[1])
    char = lineList[1][0]
    string = lineList[2]
    ''' Part 1
    if string.count(char) >= low and string.count(char) <= high:
        numValid += 1
    '''
    if (string[low-1] == char and string[high-1] != char) or (string[high-1] == char and string[low-1] != char):
        numValid += 1
print(numValid)


f.close()
