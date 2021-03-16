sugar = int(input())
bag = 0
while True:
    if sugar%5==0:
        print(bag+sugar//5)
        break
    if sugar in [3, 6, 9, 12]:
        bag+=1
        sugar-=3
    elif sugar-5<0:
        if sugar%3 ==0 :
            print(bag+sugar//3)
            break
        if sugar%3 !=0:
            print(-1)
            break
    else:
        bag+=1
        sugar-=5
'''
큰 걸 먼저 배치하려고 하지 말고,
작은 걸 먼저 배치하려고 다음부터는 시도해보자.
'''
