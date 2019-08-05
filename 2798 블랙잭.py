'''
파이썬에서 순열과 조합을 구현하는 방법
세 수 A,B,C가 있다면
순열은 AB AC BA BC CA CB가 되고,
조합은 AB, AC, BC가 된다.
파이썬에서는 이를 간단하게 계산해주는 모듈이 존재한다.
itertools의 permutations 과 combinations이다.

import itertools

chars = ['A', 'B', 'C']

p = itertools.permutations(chars, 2)  # 순열
c = itertools.combinations(chars, 2)  # 조합

print(list(p))
print(list(c))
'''
import itertools
a=list(map(int,input().split()))
sm=0
for i in itertools.combinations(list(map(int,input().split())), 3):
    s=sum(i)
    if s<=a[1] and sm<s:
        sm=s
print(sm)
    
    


