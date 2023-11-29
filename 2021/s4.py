raw_specs = [int(x) for x in input().split(' ')]
stationNum = raw_specs[0]
walkwayNum = raw_specs[1]
dayNum = raw_specs[2]

walkways = []
for x in range(walkwayNum):
    walkways.append([(int(x) - 1) for x in input().split(' ')])

stationPerm = [int(x) for x in input().split(' ')]

stationSwitches = []
for x in range(dayNum):
    stationSwitches.append([(int(x) - 1) for x in input().split(' ')])

def walkwaypath(pos, time):
    if pos == stationPerm.index(stationNum):
        return time

    actions = [w[1] for w in walkways if w[0] == pos]

    if len(actions) == 0:
        return float('inf')
    
    return min([walkwaypath(a, time + 1) for a in actions])

def travel_time():
    besttime = min(
        walkwaypath(0, float('inf')),
        stationNum - 1
        )

    print(besttime)


for x in range(dayNum):
    stationPerm[stationSwitches[x][0]], stationPerm[stationSwitches[x][1]] = stationPerm[stationSwitches[x][1]], stationPerm[stationSwitches[x][0]]
    travel_time()