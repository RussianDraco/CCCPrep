in_num = int(input("What is the input number? "))

halfNum = round(in_num / 2)

calcAr = []

restrictions = [(1/3, 2/3), (1/9, 2/9), (7/9, 8/9), (1/27, 2/27), (7/27, 8/27), (19/27, 20/27), (25/27, 26/27)]

for i in range(0, halfNum + 1):
    calcAr.append(i)
    for r in restrictions:
        Min, Max = r

        if Min < i/in_num < Max:
            calcAr.pop()
            break

for i in range(0, in_num // 2):
    calcAr.append(in_num - calcAr[i])

calcAr = set(calcAr)

for x in calcAr:
    print(x)