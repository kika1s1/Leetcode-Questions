# Problem: A - Non-Identity Permutations - https://codeforces.com/gym/523525/problem/A

t = int(input())
for i in range(t):
    n = int(input())
    data = [i for i in range(1, n+1)]
    l, r = 0, 1
    while r < len(data):
        data[l], data[r] = data[r], data[l]
        l +=2
        r +=2
    if n %2 == 0:
        print(*data)
    else:
        data[0], data[-1] = data[-1], data[0]
        print(*data)

