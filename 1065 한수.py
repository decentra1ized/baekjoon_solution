number = int(input())
def hansu(k):
    p=0
    for i in range(1, k+1) :
        if i <= 99 : 
            p += 1 
        else :     
            char = list(map(int, str(i))) 
            if char[0] - char[1] == char[1] - char[2] : 
                p += 1
    return p
print(hansu(number))
