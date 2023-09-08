import math

num_of_m = int(input())
ms = [int(x) for x in input().split(' ')] #mounts input
#out for 1, 2, 3, ... num_of_m
def find_asym_val(mounts): #asym val of list
    mn = math.floor(len(mounts) / 2) #number of mount combs
    av = 0 #output asymetry value

    for x in range(mn):
        av += abs(mounts[x] - mounts[len(mounts) - 1 - x])

    return av

print(find_asym_val(ms))