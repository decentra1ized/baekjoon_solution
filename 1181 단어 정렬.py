data = {}
index = []
for i in range(int(input())):
    k = input()
    if len(k) not in index:
        data[len(k)] = []
        index.append(len(k))
        data[len(k)].append(k)
        continue
    if k not in data:
        data[len(k)].append(k)
result =[]
index.sort()
for j in index:
    data[j].sort()
    result = result+ data[j]

for i in result:
    print(i)
