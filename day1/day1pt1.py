f = open('day1.txt', 'r')
listLines = f.readlines()
complements = {}

''' Part 1 (Two sum)
for listInt in listLines:
    val = int(listInt)
    comp = 2020-val
    if comp not in complements:
        complements[val] = comp
    else:
        print(val*comp)
'''
    

f.close()
