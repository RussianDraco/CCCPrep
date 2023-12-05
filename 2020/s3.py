og = str(input())
length = len(og)

longstring = str(input())

currentlist = 0

currentperms = {}

for i in range(len(longstring) - length + 1):
    temp = og
    
    substring = longstring[i:i+length]
  
    for i in range(length):
        if substring[i] in temp:
            truetemp = substring[i]
            temp = temp.replace(truetemp, "", 1)       
        else:
            break
        
    if temp == "" and substring not in currentperms:
        currentperms[substring] = 1
        currentlist += 1

print(currentlist)