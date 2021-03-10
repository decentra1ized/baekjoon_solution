number, limit = map(int, input().split())

def brute(k):
    if len(k) == limit:
        print(' '.join(map(str, k)))
        return 0
    for i in range(1, number+1):
        brute(k+[i])

brute([])
