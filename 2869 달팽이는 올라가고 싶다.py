a = list(map(int, input().split()))
if (a[2]-a[0])%(a[0]-a[1]) == 0:
    print((a[2]-a[0])//(a[0]-a[1])+1)
elif (a[2]-a[0])%(a[0]-a[1]) < a[0]:
    print((a[2]-a[0])//(a[0]-a[1])+2)
