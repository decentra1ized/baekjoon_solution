a, price = map(int, input().split())
coin = []
count = 0
for i in range(a):
    o = int(input())
    coin.append(o)
coin.reverse()
for i in coin:
    count += (price//i)
    price %= i
    if price == 0:
        break

print(count)

#기존 첫번째 풀이
'''
a, price = map(int, input().split())
coin = []
count = 0
for i in range(a):
    o = int(input())
    coin.append(o)
coin.reverse()
while price != 0:
    for i in coin:
        if price-i >= 0:
            price -= i
            count += 1
            break
print(count)
'''

#기존 두번째 풀이
'''
a, price = map(int, input().split())
coin = []
count = 0
for i in range(a):
    o = int(input())
    coin.append(o)
coin.reverse()
for i in coin:
    while price-i >= 0:
        price -= i
        count += 1
    if price == 0:
        break
print(count)
'''
