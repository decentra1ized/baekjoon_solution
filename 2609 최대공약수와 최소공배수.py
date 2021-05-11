def division(a, b): #유클리드 호제법
    if a%b == 0:
        return b
    else:
        return division(b, a%b)

a , b = map(int, input().split())
if a>=b:
    k = division(a, b)
else:
    k = division(b, a)

print(k)
print(a*b//k)
