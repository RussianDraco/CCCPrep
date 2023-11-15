#solving 2022 s3 for mark categories 1, 2, 3
import math

raw_vals = [int(x) for x in input().split(' ')] #input: note number, max note, sample number  -  N, M, K

note_number = raw_vals[0]
max_note = raw_vals[1] #doesn't matter for mark categories 1, 2, 3
sample_number = raw_vals[2]

def imp():
    print("-1")
    exit(0)

def solution(x): #x is an array of ints
    print(' '.join([str(y) for y in x]))
    exit(0)

if note_number > sample_number or sample_number > (note_number * (note_number + 1)) / 2:
    imp()

#check if simple solution exists
if (sqrtVal := math.sqrt(1 + 4 * (2 * (sample_number - note_number)))).is_integer():
    if sqrtVal % 2 == 1:
        #simple solution exists
        #change sqrtval to n from n(n-1)/2
        sqrtVal = int((-1 + sqrtVal)/2)
        solution([x for x in range(2, sqrtVal + 2)] + [1] * (note_number - sqrtVal))

sqrtVal = math.floor((-1 + sqrtVal)/2) #change sqrtval to n and floor it

solvingAr = [x for x in range(2, sqrtVal + 2)] + [1] * (note_number - sqrtVal)

currentSampleCount = (sqrtVal * (sqrtVal + 1)) / 2



"""
Most efficent:
piece | sampleN

1, 2 | 3
1, 2, 3 | 6
1, 2, 3, 4 | 10
1, 2, 3, 4, 5 | 15
1, 2, 3, 4, 5, 6 | 21

Therefore, if all numbers are unique, the number of good samples is (N)(N+1)/2


Least efficent:
piece | sampleN
1, 1 | 2
1, 1, 1 | 3
1, 1, 1, 1 | 4

Therefore, least efficent number of good samples in piece len N is N


For piece len N, the number of good samples is:  N <= K <= (N)(N+1)/2



Considering only 1s and 2s:

piece | sampleN

1, 1 | 2
1, 2 | 3
1, 2, 1 | 5
1, 2, 2 | 4
1, 2, 2, 1 | 5
1, 2, 1, 2 | 7
1, 1, 1, 1 | 4
1, 2, 1, 1 | 6


If 0 -> unique number and 1 -> repeated number:

piece | sampleN

0, 0 | 3
1, 1 | 2
0, 1, 1 | 4
1, 0, 1 | 5
1, 1, 0 | 4
0, 1, 0, 1 | 8

1, 1, 1, 1 | 4
0, 1, 1, 1 | 5
0, 0, 1, 1 | 7
1, 0, 1, 1 | 6
0, 1, 0, 1 | 7
1, 0, 0, 1 | 9
0, 0, 0, 0 | 10


1, 1, 1, 1, 1 | 5
0, 1, 1, 1, 1 | 6
0, 0, 1, 1, 1 | 8
0, 0, 0, 1, 1 | 11


1, 1, 1, 1, 1, 1 | 6
0, 1, 1, 1, 1, 1 | 7
0, 0, 1, 1, 1, 1 | 9
0, 0, 0, 1, 1, 1 | 12
0, 0, 0, 0, 1, 1 | 16

0 | 1, 1, 1, 1, 1, 1, 1 | 7
1 | 0, 1, 1, 1, 1, 1, 1 | 8
2 | 0, 0, 1, 1, 1, 1, 1 | 10
3 | 0, 0, 0, 1, 1, 1, 1 | 13
4 | 0, 0, 0, 0, 1, 1, 1 | 17
5 | 0, 0, 0, 0, 0, 1, 1 | 22
"""