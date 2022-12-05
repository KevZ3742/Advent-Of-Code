top = ""
stacks = []

with open('Day5-SupplyStacks.txt') as file:
    crates, procedure = file.read().split("\n\n")

    for line in crates.splitlines():
        for counter, i in enumerate(range(1, len(line), 4)):
            while counter >= len(stacks):
                stacks.append([])

            if line[i] != " ":
                stacks[counter].append(line[i])

    for line in procedure.splitlines():
        instructions = [int(s) for s in line.split() if s.isdigit()]

        temp = []
        for i in range(instructions[0]):
            temp.insert(0, stacks[instructions[1] - 1].pop(0))
        
        count = 0
        for i in temp:
            stacks[instructions[2] - 1].insert(0, temp[count])
            count += 1

    for i in stacks:
        top += i[0]

    print(top)
