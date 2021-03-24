import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
for i in sorted(data):
    sys.stdout.write(str(i)+'\n')
