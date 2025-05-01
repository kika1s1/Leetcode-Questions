# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A

t = int(input())
for i in range(t):
    data = int(input())
    if data == 1:
        print(2)
    elif data % 3 == 0:
        print(data // 3)
    else:
        print(data // 3 + 1)
