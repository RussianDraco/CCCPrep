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
"""