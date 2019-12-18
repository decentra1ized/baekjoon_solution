#재귀함수를 쓴 풀이
def fibo(a):
    if a==0:
        return 0;
    elif a==1 or a==2:
        return 1;
    return fibo(a-1) + fibo(a-2)
print(fibo(int(input())))

#재귀함수는 아니지만 기본적인 원리는 동일한 풀이

a = int(input())
fibo = [0,1]
for i in range(0, a-1):
    fibo.append(fibo[i]+fibo[i+1])
    print(fibo)

print(fibo[a])
    
