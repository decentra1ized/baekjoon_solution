import sys
sys.setrecursionlimit(10**9)

a = int(input())
array = [[0] * a for i in range(a)]

def delblock(d):
    for i in range(d, d*2):
        for l in range(d, d*2):
            array[i][l] = 0

def addblock(n, r, c):
    if n == 3:
        array[r][0+c] = 1
        array[r][1+c] = 1
        array[r][2+c] = 1
        array[r+1][0+c] = 1
        array[r+1][2+c] = 1
        array[r+2][0+c] = 1
        array[r+2][1+c] = 1
        array[r+2][2+c] = 1
    else:
        for k in range(0, a, 3):
            for j in range(0, a, 3):
                addblock(a//3, k, j)
        delblock(a//3)

addblock(a, 0, 0)

for i in range(a):
    for j in range(a):
        if array[i][j]==1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

