# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

x = int(input())
  
for i in range(x):
    n = int(input())
    if n == 1:
        print(3)
    else:
        if n%2 == 1:
            print(1)
        else:
            init = 0
            num = n
            while n%2==0:
                init += 1
                n //= 2
            t = 2**init
            if t == num:
                print(t+1)
            else:
                print(t)