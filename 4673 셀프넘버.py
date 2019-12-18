l = list(range(1,10001))
k=0

def selfnum(n):
    st = str(n)
    if len(st) == 1:
        return int(2*n)
    elif len(st) == 2:
        return n+int(st[0])+int(st[1])
    elif len(st) == 3:
        return n+int(st[0])+int(st[1])+int(st[2])
    elif len(st) == 4:
        return n+int(st[0])+int(st[1])+int(st[2])+int(st[3])
    elif len(st) == 5:
        return n+int(st[0])+int(st[1])+int(st[2])+int(st[3])+int(st[4])
    
for i in range(1, 10001):
    k = selfnum(i)
    if k in l:
        l.remove(k)
for j in l:
    print(j)

#내가 일렬로 나열한 풀이과정들

#다른 사람이 푼 숏코딩
r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))
