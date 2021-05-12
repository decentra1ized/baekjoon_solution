a, b = map(int, input().split())
k = list(map(int, input().split()))
for i in k:
    print(i - a*b, end=" ")
