num = int(input())
l = []
for i in range(num):
    l.append(int(input()))
l.sort()
for i in range(num):
    print(l[i])
