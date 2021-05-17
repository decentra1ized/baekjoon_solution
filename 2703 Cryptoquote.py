while True:
    a = int(input())
    for i in range(a):
        b = str(input())
        data = list(str(input()))
        k = ''
        for i in range(len(b)):
            if ord(b[i]) < 65:
                k += ' '
            else:
                k += data[ord(b[i]) - 65]
        print(k)
    break
