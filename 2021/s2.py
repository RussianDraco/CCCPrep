rows = int(input())
cols = int(input())
inNum = int(input())
changes = []

for x in range(inNum):
    changes.append(input().split(" "))

canvas = [[False for x in range(cols)] for y in range(rows)]

for chng in changes:
    lineNum = int(chng[1]) - 1
    if chng[0] == "R":
        for x in range(len(canvas[lineNum])):
            canvas[lineNum][x] = not canvas[lineNum][x]
    elif chng[0] == "C":
        for x in range(rows):
            canvas[x][int(chng[1]) - 1] = not canvas[x][int(chng[1]) - 1]

n = 0
for x in canvas:
    for y in x:
        if y:
            n += 1

print(n)