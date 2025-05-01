# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())  
    data = list(map(int, input().split())) 
    
    cnt = [0] * 32 
    for d in data:
        for i in range(32):
            cnt[i] += (1 - ((d >> i) & 1))
    for i in range(30, -1, -1):
        if k >= cnt[i]:
            k -= cnt[i]
            cnt[i] = 0
    
    ans = 0  
    for i in range(32):
        if cnt[i] == 0:
            ans += (1 << i)
    
    print(ans)