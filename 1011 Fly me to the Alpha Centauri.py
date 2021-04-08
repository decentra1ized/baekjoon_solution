for i in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    count = 0  
    move = 1  
    add = 0  
    while add < distance :
        count += 1
        add += move  
        if count % 2 == 0 : 
            move += 1  
    print(count)
