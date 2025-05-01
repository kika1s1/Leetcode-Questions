# Problem: F - Messi versus Ronaldo - https://codeforces.com/gym/522079/problem/F

mod = (10**9) + 7

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    bits = [0]*64
    for num in arr:
        for i in range(64):
            if num & (1 << i):
                bits[i] += 1
    ans = 0
    for i in range(n):
        or_sum = 0
        and_sum = 0
        temp = arr[i]
        for j in range(64):
            if temp & (1 << j):
                and_sum += ((1 << j) % mod * bits[j] % mod) % mod
                or_sum += ((1 << j) % mod * n % mod) % mod
            else:
                or_sum += ((1 << j) % mod * bits[j] % mod) % mod
            
        ans += (or_sum* and_sum) % mod
    
    print(ans % mod)


    # ans = 0
    # for i in range(n):
    #     for j in range(n):
    #         and_val = arr[i] & arr[j]
    #         or_val = arr[i] | arr[j]
    #         for k in range(n):
    #             ans += and_val * or_val
    #             ans %= mod
    # print(ans)