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
