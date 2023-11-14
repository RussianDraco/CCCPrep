#solving 2022 s3 for mark categories 1, 2, 3

raw_vals = [int(x) for x in input().split(' ')]

note_number = raw_vals[0]
max_note = raw_vals[1] #dosent matter for mark categories 1, 2, 3
sample_number = raw_vals[2]

def imp():
    print("-1")
    exit(0)

if note_number > sample_number or sample_number > (note_number * (note_number + 1)) / 2:
    imp()

piece_ar = [1] * note_number
current_samples = note_number
sample_contribution = [1] * note_number
sample_makeup = sample_number - note_number

while current_samples != sample_number:
    piece_ar



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

1, 1, 1, 1, 1, 1, 1 | 7
0, 1, 1, 1, 1, 1, 1 | 8
0, 0, 1, 1, 1, 1, 1 | 10
0, 0, 0, 1, 1, 1, 1 | 13
0, 0, 0, 0, 1, 1, 1 | 17
0, 0, 0, 0, 0, 1, 1 | 22
"""