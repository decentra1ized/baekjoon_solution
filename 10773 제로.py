a = int(input())
data = []
for i in range(a):
    num = int(input())
    if num == 0:
        data.pop()
    else:
        data.append(num)
print(sum(data))
