total = 0

with open('Day2-RockPaperScissors.txt') as file:
    for line in file:
        line = line.strip().split(' ')

        if line[0] == "A":
            line[0] = "X"
        if line[0] == "B":
            line[0] = "Y"
        if line[0] == "C":
            line[0] = "Z"

        if line[0] == line[1]:
            total = total + 3
        elif line[1] == "X":
            if line[0] == "Z":
                total = total + 6
        elif line[1] == "Y":
            if line[0] == "X":
                total = total + 6
        elif line[1] == "Z":
            if line[0] == "Y":
                total = total + 6

        if line[1] == "X":
            total = total + 1
        if line[1] == "Y":
            total = total + 2
        if line[1] == "Z":
            total = total + 3

print(total)