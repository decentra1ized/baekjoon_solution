a = int(input())
for i in range(a):
    customer = list(map(int, input().split()))
    h = customer[0]
    w = customer[1]
    n = customer[2]
    a = n % h
    b = n//h + 1
    if a==0:
        a = h
        b -= 1
    print(a*100+b)
        
    
