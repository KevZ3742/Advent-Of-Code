file = open("Day6-TuningTrouble.txt", "r")

def fourMarker(file):
    line = file.read()
    for i in range(len(line)):
        if len(set(line[i - 4 : i])) == 4:
            return i

print(fourMarker(file))
file.close()