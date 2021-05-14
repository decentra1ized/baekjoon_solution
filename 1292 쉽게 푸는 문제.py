a, b = map(int, input().split())
data = []
for i in range(1, int(b*1/2)+2):
    for j in range(i):
        data.append(i)
print(sum(data[a-1:b]))
