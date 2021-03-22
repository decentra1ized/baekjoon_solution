bs=int(input())

row=1
while bs>row:
    bs-=row
    row+=1
    
if row%2==0:
    a=bs
    b=row-bs+1
else:
    a=row-bs+1
    b=bs
    
print(int(a)+'/'+int(b))
