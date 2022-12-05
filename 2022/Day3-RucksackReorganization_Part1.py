import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

sum = 0
sack = ["", ""]

with open('Day3-RucksackReorganization.txt') as file:
    for line in file:
        line = line.strip()

        sack[0] = line[:int(len(line)/2)]
        sack[1] = line[int(len(line)/2):len(line)]

        for var in range(len(sack[0])):
            if(sack[0][var] in sack[1]):
                sum = sum + values[sack[0][var]]
                break
        
print(sum)