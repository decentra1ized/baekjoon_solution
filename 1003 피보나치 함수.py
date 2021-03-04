result = []
for k in range(int(input())):
    n = int(input())
    zero = [1] + [0] * 40
    one = [0, 1] + [0] * 49

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    result.append([zero[n], one[n]])

for i in result:
    print(i[0], i[1])
    
#아래 처럼 복잡하게 풀지 않아도 될 것 같다. 굳이 메모이제이션 피보나치까지 구현해서 일일히 해줄 필요 없음.
'''
a = int(input())

one = 0
zero = 0

dic = {0:0,1:1}
count = {0:[1,0], 1:[0,1]}

def fibo_memo(n):
    global one
    global zero
    if n in dic:
        zero += count[n][0]
        one += count[n][1] 
        return dic[n]
    dic[n] = fibo_memo(n-1) + fibo_memo(n-2)
    count[n] = [count[n-1][0] + count[n-2][0],count[n-1][1] + count[n-2][1]]
    return dic[n]

result = [0] * a
for i in range(a):
    one = 0
    zero = 0
    k = int(input())
    fibo_memo(k)
    result[i] = str(zero)+" "+str(one)

print('\n'.join(result))
'''
