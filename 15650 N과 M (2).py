a, b = map(int, input().split())

k = [0] * b

def brute(index, start, n, m):
    if index == b:
        for j in k:
            if k.count(j) > 1:
                return 0
        print(' '.join(map(str, k)))     
        return 0
    for i in range(start, len(n)):
        k[index] = n[i]
        brute(index+1, i+1, n, m)
        
number = list(range(a+1))
number.remove(0)

brute(0, 0, number, b)
