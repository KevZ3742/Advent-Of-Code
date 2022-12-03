import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

sum = 0
sack = ["", "", ""]

counter = 0

with open('Day3-RucksackReorganization.txt') as file:
    for line in file:
        line = line.split('\n')

        sack[counter] = line[0]

        counter = counter + 1

        if(counter == 3):
            for var in range(len(sack[0])):
                if(sack[0][var] in sack[1] and sack[0][var] in sack[2]):
                    sum = sum + values[sack[0][var]]
                    break

            counter = 0
        
print(sum)