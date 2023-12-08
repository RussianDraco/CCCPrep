ppl = input()

#Example: BABCBCACCA -> AABCBCBCCA -> AABBBCCCCA (2 swaps)

ANum = ppl.count('A') #3
BNum = ppl.count('B') #3
CNum = ppl.count('C') #4

print("BABCBCACCA"[0:3])

for x in range(len(ppl)):
    if ppl[x:x+ANum].count('A') == ANum:
        pass