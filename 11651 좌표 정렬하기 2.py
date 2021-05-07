a = int(input())
data = []
for i in range(a):
    x, y = map(int, input().split())
    data.append([y, x])

data.sort()

for i in data:
    print(i[1], i[0])
