rows = int(input())
cols = int(input())
inNum = int(input())
changes = []

for x in range(inNum):
    changes.append(input().split(" "))

canvas = [[0 for x in range(cols)] for y in range(rows)]

for chng in changes:
    lineNum = int(chng[1])
    if chng[0] == "R":
        for x in canvas[lineNum]
    elif chng[0] == "C":
        for x in range(rows):
            canvas[x][int(chng[1])] += int(chng[2])