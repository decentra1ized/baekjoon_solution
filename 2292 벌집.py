import math
a = int(input())

i = 0
k = 2

if a==1:
    print(1)
else:
    while True:
        i += 1
        k = k + 6*i
        if k > a:
            print(i+1)
            break
