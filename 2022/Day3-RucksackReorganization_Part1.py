import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

sum = 0
sack = ["", ""]

with open('Day3-RucksackReorganization.txt') as file:
    for line in file:
        line = line.split('\n')

        sack[0] = line[0][:int(len(line[0])/2)]
        sack[1] = line[0][int(len(line[0])/2):len(line[0])]

        for var in range(len(sack[0])):
            if(sack[0][var] in sack[1]):
                sum = sum + values[sack[0][var]]
                break
        
print(sum)