import random

rawvals = [int(x) for x in input().split(' ')]
height = rawvals[0]
width = rawvals[1]

palin_rows = rawvals[2]
palin_cols = rawvals[3]

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

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

    return [ncols, nrows]

def make_simple_pal(c1, c2, l): #char1, char2, length
    return c1 + c2 * (l - 2) + c1

def imp():
    print("IMPOSSIBLE")
    exit(0)

if palin_cols > width or palin_rows > height: imp()

grid = [["a" for y in range(width)] for x in range(height)]

if palin_cols == 0 or palin_rows == 0:
    cur_char_pos = 0
    for i in range(height):
        for j in range(width):
            grid[i][j] = ALPHABET[cur_char_pos]
            if width % 26 == 0: cur_char_pos = (cur_char_pos + 3) % 25 
            else: cur_char_pos = (cur_char_pos + 1) % 25
        if grid[i][0] == ALPHABET[cur_char_pos]:
            cur_char_pos = (cur_char_pos + 1) % 25

    if palin_cols == 0 and palin_rows == 0:
        pass

    elif palin_cols == 0:
        cur_char_pos = 0
        n = 0
        while calc_grid(grid)[1] < palin_rows:
            grid[n] = list(make_simple_pal(ALPHABET[cur_char_pos], ALPHABET[(cur_char_pos + 1) % 25], width))
            cur_char_pos = (cur_char_pos + 1) % 25
            n+=1

    elif palin_rows == 0:
        cur_char_pos = 0
        n = 0
        while calc_grid(grid)[0] < palin_cols:
            pal = make_simple_pal(ALPHABET[cur_char_pos], ALPHABET[(cur_char_pos + 1) % 25], height)

            for x in range(height):
                grid[x][n] = pal[x]
            
            cur_char_pos = (cur_char_pos + 1) % 25
            n+=1

else:
    rm_col_pals = width - palin_cols
    rm_row_pals = height - palin_rows

    grid[-1] = list("a" * palin_cols + "b" * rm_col_pals)

    for x in range(rm_row_pals):
        grid[len(grid) - 1 - x][-1] = "b"

fincalc = calc_grid(grid)

if fincalc[0] != palin_cols or fincalc[1] != palin_rows:
    imp()

print('\n'.join([''.join(x) for x in grid]))