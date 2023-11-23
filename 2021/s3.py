pplNum = int(input())
ppl = []

for x in range(pplNum):
    ppl.append([int(x) for x in input().split(' ')]) #position, speed(1 unit per x seconds), hearing distance

avg_pos = round(sum([(x[0]*x[1]) for x in ppl])/pplNum)

time = 0

for p in ppl:
    if (p[0] - p[2]) <= avg_pos <= (p[0] + p[2]):
        continue
    else:
        if avg_pos < (p[0] - p[2]):
            time += p[1] * (p[0] - p[2] - avg_pos)
        elif avg_pos > (p[0] + p[2]):
            time += p[1] * (avg_pos - (p[0] + p[2]))

print(time)