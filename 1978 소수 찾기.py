a = int(input())
count = 0
for i in list(map(int, input().split(' '))):
    if i == 1:
        continue
    elif i == 2:
        count=count+1
    else:
        l = list(range(2, int(i/2)+1))
        for j in range(2, int(i/2)+1):
            if i%j!=0:
                l.remove(j)
        if len(l) == 0:
            count = count + 1
            
        
print(count)

#에라토스테네스의 체

n = int(input())
numbers = {int(x) for x in input().split()}
prime = {i for i in range(2,1001)}
for i in range(2, 34):
    k = 2
    while i*k <= 1000:
        prime.discard(i*k)
        k += 1
        
print(len(numbers&prime))

#실제로 모든 소수를 다 구해놓고 주어진 범위 내에 있는 애들의 개수를 세줌
#리스트 안에 for문을 포함하는 리스트 내포(List comprehension)
'''
>>> a = [1,2,3,4]
>>> result = [num * 3 for num in a]
>>> print(result)
[3, 6, 9, 12]

만약 [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 리스트 내포 안에 "if 조건"을 사용할 수 있다.
'''
