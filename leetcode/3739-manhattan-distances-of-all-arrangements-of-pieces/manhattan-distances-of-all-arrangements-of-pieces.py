class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 10**9 + 7
        r = m * n
        
        fact = [1] * (r + 1)
        invfact = [1] * (r + 1)
        for i in range(2, r + 1):
            fact[i] = fact[i - 1] * i % mod
        invfact[r] = pow(fact[r], mod - 2, mod)
        for i in range(r, 0, -1):
            invfact[i - 1] = invfact[i] * i % mod

        def comb(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            return fact[n_val] * invfact[r_val] % mod * invfact[n_val - r_val] % mod

        ways = comb(r - 2, k - 2)
        
        inv6 = pow(6, mod - 2, mod) 
        
        S_rows = (n * n % mod) * ((m - 1) * m % mod) % mod * ((m + 1) % mod) % mod * inv6 % mod
        S_cols = (m * m % mod) * ((n - 1) * n % mod) % mod * ((n + 1) % mod) % mod * inv6 % mod
        total = (S_rows + S_cols) % mod

        return ways * total % mod
