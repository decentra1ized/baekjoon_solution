xlist = []
ylist = []
for i in range(3):
        x, y = map(int, input().split())
        xlist.append(x)
        ylist.append(y)
for j in range(3):
        if xlist.count(xlist[j]) == 1:
                a = xlist[j]
        if ylist.count(ylist[j]) == 1:
                b = ylist[j]
print(a, b)
