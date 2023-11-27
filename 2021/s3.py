pplNum = int(input())
ppl = []

for x in range(pplNum):
    ppl.append([int(x) for x in input().split(' ')]) #position, speed(1 unit per x seconds), hearing distance

allPos = [x[0] for x in ppl]

smallP, bigP = min(allPos), max(allPos)

besttime = float('inf')
for x in range(smallP, bigP+1):
    totaltime = 0

    for p in ppl:
        parttime = 0
        if p[0] < x:
            if (p[0] + p[2]) > x:
                continue
            else:
                totaltime += (x - (p[0] + p[2])) * p[1]
        elif p[0] > x:
            if (p[0] - p[2]) < x:
                continue
            else:
                totaltime += ((p[0] - p[2]) - x) * p[1]
        elif p[0] == x:
            continue

    besttime = min(besttime, totaltime)

print(besttime)