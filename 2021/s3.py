pplNum = int(input())
ppl = []

for x in range(pplNum):
    ppl.append([int(x) for x in input().split(' ')]) #position, speed(1 unit per x seconds), hearing distance

allPos = [x[0] for x in ppl]

smallP, bigP = min(allPos), max(allPos)

def all_dist(x):
    totaltime = 0

    for p in ppl:
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

    return totaltime

bestdist = float('inf')

left = smallP
right = bigP
while left <= right:
    mid = (left + right) // 2
    
    left_t = all_dist(mid - 1)
    mid_t = all_dist(mid)
    right_t = all_dist(mid + 1)

    if mid_t < left_t and mid_t < right_t:
        bestdist = mid_t
        break
    elif left_t == mid_t or right_t == mid_t:
        bestdist = mid_t
        break
    elif mid_t <= right_t:
        right = mid - 1
    else:
        left = mid + 1

print(bestdist)