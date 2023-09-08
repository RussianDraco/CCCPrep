import random

rawvals = [int(x) for x in input().split(' ')]
print()
height = rawvals[0]
width = rawvals[1]

palin_cols = rawvals[2]
palin_rows = rawvals[3]

def is_pal(s): return (s[::-1] == s)

def calc_grid(grd): #return n in cols, n in rows
    ncols = 0
    nrows = 0

    for r in grd:
        if is_pal(''.join(r)): nrows += 1

    grd2 = [[] for y in range(width)]

    for r in grd:
        for x in range(len(r)):
            grd2[x].append(r[x])

    for r in grd2:
        if is_pal(''.join(r)): ncols += 1

    return (ncols, nrows)

def imp():
    print("IMPOSSIBLE")
    exit(0)

if palin_cols > width or palin_rows > height: imp()

grid = [["a" for y in range(width)] for x in range(height)]

t = 0

while calc_grid(grid) != (palin_cols, palin_rows):
    grid[random.randint(0, height - 1)][random.randint(0, width - 1)] = ["a", "b", "c"][random.randint(0, 2)]
    t += 1
    print(str(t))
    print('\n'.join([' '.join(x) for x in grid]))

print(str(t))
print('\n'.join([' '.join(x) for x in grid]))