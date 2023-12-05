from collections import deque, defaultdict

rowNum = int(input())
colNum = int(input())

rows = []
for i in range(rowNum):
    rows.append([int(x) for x in input().split(' ')])

dict = defaultdict(list)
xn = 1
for x in rows:
    yn = 1
    for y in x:
        dict[y].append((xn, yn))
        yn += 1
    xn += 1

visited = {}
q = deque()
q.append((colNum, rowNum))

while q:
    row, col = q.popleft()
    if row == 1 and col == 1:
        print('yes')
        exit(0)
    if visited.get((row, col)) == True:
        continue
    visited[(row, col)] = True
    g = dict.get(row * col)
    if not len(g) == 0:
        for x, y in g:
            if not visited.get((x, y)) == True:
                q.append((x, y))
print('no')