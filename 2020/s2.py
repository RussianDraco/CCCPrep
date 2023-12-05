from collections import deque, defaultdict

rowNum = int(input())
colNum = int(input())

largestNum = max(rowNum, colNum)

rows = []
for i in range(rowNum):
    rows.append([int(x) for x in input().split(' ')])

def factors(n):
    for x in range(1, min(largestNum, n + 1)):
        if n % x == 0:
            if x <= largestNum and int(n / x) <= largestNum:
                yield (int(x), int(n / x))

dict = defaultdict(set)
for x in rows:
    for y in x:
        [dict[y].add((xn, yn)) for xn, yn in factors(y)]

visited = {}
q = deque()
q.append((1, 1))

while q:
    print(str(q))
    row, col = q.popleft()
    if row == rowNum and col == colNum:
        print('yes')
        exit(0)
    if visited.get(rows[row - 1][col - 1]) == True:
        continue
    visited[rows[row - 1][col - 1]] = True
    g = list(dict.get(rows[row - 1][col - 1]))
    if not len(g) == 0:
        for x, y in g:
            if not visited.get(rows[x - 1][y - 1]) == True:
                q.append((x, y))
print('no')