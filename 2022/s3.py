raw_vals = [int(x) for x in input().split(' ')]

note_number = raw_vals[0]
max_note = raw_vals[1]
sample_number = raw_vals[2]

def imp():
    print("-1")
    exit(0)

if note_number > (2*max_note-1):
    imp()

