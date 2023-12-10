pcnum = int(input())
changes = []

for x in range(pcnum):
    changes.append([int(x) for x in input().split(' ')])

changes.sort(key=lambda x: x[0])

b = 0
for i, v in enumerate(changes[1:]):
    b = max(b, abs((v[1] - changes[i][1]) / (v[0] - changes[i][0])))

print(b)