# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

def max_ribbon_pieces(n, a, b, c):
    dp = [-float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i >= a:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c:
            dp[i] = max(dp[i], dp[i - c] + 1)
    
    return dp[n]


n, a, b, c = map(int, input().split())

print(max_ribbon_pieces(n, a, b, c))
