num = int(input())
l = []
for i in range(num):
    l.append(int(input()))
for i in sorted(l):
    print(i)
'''
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
for i in sorted(data):
    sys.stdout.write(str(i)+'\n')
'''
