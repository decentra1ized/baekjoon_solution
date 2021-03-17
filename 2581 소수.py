a=int(input())
b=int(input())
array=[]

for i in range(a,b+1):
    if i == 1:
        pass
    elif i == 2:
        array.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == (i-1):
                array.append(i)

if len(array)==0:
    print('-1')
else:
    print(sum(array))
    print(min(array))
