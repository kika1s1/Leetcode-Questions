# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

def solve():
    n, k, x = map(int, input().split())
    
    if x != 1:
        print("YES")
        print(n)
        print(' '.join(['1'] * n))
    elif n % 2 == 1 and k == 2:
        print("NO")
    elif k == 1:
        print("NO")
    else:
        print("YES")
        print(n // 2)
        result = ['2'] * (n // 2-1)
        result.append(str(2 + (n % 2)))
        print(' '.join(result))

t = int(input())
for i in range(t):
    solve()
