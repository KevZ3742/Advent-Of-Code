elvesCalories = []

tempTotalCalories = 0
tempCalories = 0

with open('Day1-CalorieCounting.txt') as file:
    for line in file:
        line = line.split('\n')

        if(line[0] == ""):
            elvesCalories.append(tempTotalCalories)
            tempTotalCalories = 0
        else:
            tempTotalCalories = tempTotalCalories + int(line[0])

elvesCalories.sort(reverse=True)

print(elvesCalories[0])