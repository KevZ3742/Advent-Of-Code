total = 0

with open('RockPaperScissors.txt') as file:
    for line in file:
        line = line.split('\n')[0].split(' ')

        if line[0] == "A":
            line[0] = "X"
        if line[0] == "B":
            line[0] = "Y"
        if line[0] == "C":
            line[0] = "Z"

        if line[0] == "X":
            if line[1] == "X":
                total = total + 3
            if line[1] == "Y":
                total = total + 1
            if line[1] == "Z":
                total = total + 2
        if line[0] == "Y":
            if line[1] == "X":
                total = total + 1
            if line[1] == "Y":
                total = total + 2
            if line[1] == "Z":
                total = total + 3
        if line[0] == "Z":
            if line[1] == "X":
                total = total + 2
            if line[1] == "Y":
                total = total + 3
            if line[1] == "Z":
                total = total + 1

        #draw
        if line[1] == "Y":
            total = total + 3
        #win
        if line[1] == "Z":
            total = total + 6

print(total)