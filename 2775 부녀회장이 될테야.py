a = int(input())
result=[]

for i in range(a):
    n = int(input())
    k = int(input())
    level = list(range(1, k+1))
    for j in range(n):
        for m in range(1,k):
            level[m] += level[m-1]
    result.append(str(level[-1]))

print('\n'.join(result))
