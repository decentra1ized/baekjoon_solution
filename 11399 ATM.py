num = int(input())
data = list(map(int, input().split()))
data.sort()
result=0
for i in range(num):
    result += (num-i) * data[i]
print(result)
                
