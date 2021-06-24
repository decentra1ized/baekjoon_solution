a = int(input())

data = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(data)):
    if a >= data[i]:
        count += 1
        a -= data[i]
    if a == 0:
        break
    
print(count)
