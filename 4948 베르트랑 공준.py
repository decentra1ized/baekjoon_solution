def prime(b):
    k = 0
    for i in range(b+1, b*2 + 1):
        if data[i]:
            k += 1
    print(k)

n = 123456*2 + 1
data = [1]*n
for i in range(2, int(n**0.5)+1):
    if data[i]:
        for j in range(2*i, n, i):
            data[j] = 0

while True:
    a = int(input())
    if a == 0:
        break
    prime(a)
