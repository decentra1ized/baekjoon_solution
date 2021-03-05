k=[]
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    if b>a and (b%a==0):
        k.append("factor")
    elif a>b and (a%b==0):
        k.append("multiple")
    else:
        k.append("neither")
for i in k:
    print(i)
