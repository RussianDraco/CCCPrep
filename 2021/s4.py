raw_specs = [int(x) for x in input().split(' ')]
stationNum = raw_specs[0] - 1
walkwayNum = raw_specs[1]
dayNum = raw_specs[2]

walkways = []
for x in range(walkwayNum):
    walkways.append([(int(x) - 1) for x in input().split(' ')])

stationPerm = [(int(x) - 1) for x in input().split(' ')]

stationSwitches = []
for x in range(dayNum):
    stationSwitches.append([(int(x) - 1) for x in input().split(' ')])

def walkwaypath(pos, time):
    if pos == stationPerm.index(stationNum):
        print(str(pos))
        print(str(stationPerm.index(stationNum)))
        return time

    actions = [w[1] for w in walkways if w[0] == pos]

    if len(actions) == 0:
        return float('inf')

    if stationPerm.index(stationNum) in actions:
        return walkwaypath(stationPerm.index(stationNum), time + 1)

    return min([walkwaypath(a, time + 1) for a in actions])

def combopath():
    return min([walkwaypath(stationPerm.index(w[0]), stationPerm.index(w[0])) for w in walkways])

def travel_time():
    besttime = min(
        combopath(),
        stationNum
        )

    print(besttime)


for x in range(dayNum):
    stationPerm[stationSwitches[x][0]], stationPerm[stationSwitches[x][1]] = stationPerm[stationSwitches[x][1]], stationPerm[stationSwitches[x][0]]
    print(str(stationPerm))
    travel_time()