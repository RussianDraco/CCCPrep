from collections import deque, defaultdict

rowNum = int(input())
colNum = int(input())

largestNum = max(rowNum, colNum)

rows = []
for i in range(rowNum):
    rows.append([int(x) for x in input().split(' ')])

def factors(n):
    for x in range(1, n + 1):
        if n % x == 0:
            if x <= rowNum and int(n / x) <= colNum:
                yield (int(x), int(n / x))

dict = defaultdict(set)
for x in rows:
    for y in x:
        [dict[y].add((xn, yn)) for xn, yn in factors(y)]

visited = {}
q = deque()
q.append((1, 1))

while q:
    row, col = q.popleft()
    if row == rowNum and col == colNum:
        print('yes')
        exit(0)
    if visited.get(rows[row - 1][col - 1]) == True:
        continue
    visited[rows[row - 1][col - 1]] = True
    g = dict.get(rows[row - 1][col - 1])
    if not g == None:
        for x, y in list(g):
            if not visited.get(rows[x - 1][y - 1]) == True:
                q.append((x, y))
print('no')