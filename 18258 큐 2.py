import sys
array = []

def push(n):
    array.append(n)

def pop():
    if array == []:
        print(-1)
    else:
        print(array.pop(0))
    
def size():
    print(len(array))

def empty():
    if array == []:
        print(1)
    else:
        print(0)

def front():
    if array == []:
        print(-1)
    else:
        print(array[0])

def back():
    if array == []:
        print(-1)
    else:
        print(array[-1])

a = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range()]
for cmd in range(a):
    if cmd == "front":
        front()
    elif cmd == "back":
        back()
    elif cmd == "pop":
        pop()
    elif cmd == "empty":
        empty()
    elif cmd == "size":
        size()
    else:
        b = cmd.split()
        push(int(b[1]))
