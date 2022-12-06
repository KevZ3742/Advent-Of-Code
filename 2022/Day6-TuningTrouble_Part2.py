file = open("Day6-TuningTrouble.txt", "r")

def fourteenMarker(f):
    line = f.read()
    for i in range(len(line)):
        if len(set(line[i - 14 : i])) == 14:
            return i

print(fourteenMarker(file))