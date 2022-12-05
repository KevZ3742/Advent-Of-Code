import re

total = 0
count = 0

with open('Day4-CampCleanup.txt') as file:
    for line in file:
        count = count + 1
        line = line.strip()
        line = re.split('-|,', line)
        line = [int(a) for a in line]

        if(all(e in range(line[0], line[1]+1) for e in range(line[2], line[3]+1))):
            total = total + 1
        elif(all(e in range(line[2], line[3]+1) for e in range(line[0], line[1]+1))):
            total = total + 1

print(total)