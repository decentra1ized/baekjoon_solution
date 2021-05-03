l = int(input())
data = []
num = 0
tail = 0
for i in range(l):
    a, b = map(int, input().split())
    data.append([a, b])
data = sorted(data, key=lambda k: k[0])
data = sorted(data, key=lambda k: k[1])

for i in range(l):
    if data[i][0] >= tail:
        num += 1
        tail = data[i][1]
        print(tail)
print(num)
