a, b = map(int, input().split())
for i in range(a, b+1):
    k = True
    if i==1:
        continue
    else:
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                k = False
                break
        if k == True:
            print(i)
