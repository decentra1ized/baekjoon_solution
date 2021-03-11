number, limit = map(int, input().split())

def brute(k):
    if len(k) not in [0,1]:
        if k[len(k)-2] > k[len(k)-1]:
            return 0
    if len(k) == limit:
        print(' '.join(map(str, k)))
        return 0
    for i in range(1, number+1):
        brute(k+[i])

brute([])
