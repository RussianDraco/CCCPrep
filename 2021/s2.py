rows = int(input())
cols = int(input())
inNum = int(input())

colswipes = [False] * cols
rowswipes = [False] * rows

for i in range(inNum):
    inp = input().split()
    index = int(inp[1]) - 1
    if inp[0] == "R":
        rowswipes[index] = not rowswipes[index]
    elif inp[0] == "C":
        colswipes[index] = not colswipes[index]

canvas = [[False for x in range(cols)] for y in range(rows)]

for i in range(rows):
    if rowswipes[i]:
        for j in range(cols):
            canvas[i][j] = not canvas[i][j]

for i in range(cols):
    if colswipes[i]:
        for j in range(rows):
            canvas[j][i] = not canvas[j][i]

n = 0
for x in canvas:
    for y in x:
        if y:
            n += 1

print(n)