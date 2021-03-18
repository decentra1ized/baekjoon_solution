import sys
a = list(map(int, sys.stdin.readline().split()))

if a[1]>=a[2]:
    i=-1
else:
    i = (a[0]//(a[2]-a[1])+1)

print(i)
