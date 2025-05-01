# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B




def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        maxim = float("-inf")
        dp = [0] * n  
        for i in range(n-1, -1, -1):
            if i + arr[i] >= n:
                dp[i] = arr[i] 
            else:
                dp[i] = arr[i] + dp[i + arr[i]]  
            maxim = max(maxim, dp[i])

        print(maxim)

main()