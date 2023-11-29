raw_specs = [int(x) for x in input().split(' ')]
stationNum = raw_specs[0]
walkwayNum = raw_specs[1]
dayNum = raw_specs[2]

walkways = []
for x in range(walkwayNum):
    walkways.append([int(x) for x in input().split(' ')])

stationPerm = [int(x) for x in input().split(' ')]

stationSwitches = []
for x in range(dayNum):
    stationSwitches.append([int(x) for x in input().split(' ')])

def travel_time_helper(pos, trainPos, stations, curtime):
    if stations[pos] == stationNum:
        return curtime
    if trainPos > stations.index(stationNum):
        return float('inf')

    actions = [[w[0]-1, w[1]-1] for w in walkways if w[0] == pos]
    if pos == trainPos:
        actions.append([pos, pos+1])

    if len(actions) == 0:
        return float('inf')

    return min([travel_time_helper(a[1], trainPos + 1, stations, curtime + 1) for a in actions])


def travel_time(stations):
    besttime = travel_time_helper(0, 0, stations, 0)
    print(besttime)


for x in range(dayNum):
    stationPerm[stationSwitches[x][0] - 1], stationPerm[stationSwitches[x][1] - 1] = stationPerm[stationSwitches[x][1] - 1], stationPerm[stationSwitches[x][0] - 1]
    travel_time(stationPerm)