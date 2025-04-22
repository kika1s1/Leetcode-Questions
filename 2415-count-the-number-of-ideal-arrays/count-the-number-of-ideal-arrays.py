MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # Precompute all primes up to maxValue using Sieve
        primes = []
        is_prime = [True] * (maxValue + 1)
        for i in range(2, maxValue + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i*i, maxValue + 1, i):
                    is_prime[j] = False

        # Function to get prime factor counts (exponents)
        def prime_factors(x):
            factors = Counter()
            for p in primes:
                if p * p > x:
                    break
                while x % p == 0:
                    factors[p] += 1
                    x //= p
            if x > 1:
                factors[x] += 1
            return list(factors.values())

        ans = 0
        for x in range(1, maxValue + 1):
            ways = 1
            for exp in prime_factors(x):
                # Stars and bars: C(n + exp - 1, exp)
                ways = ways * comb(n + exp - 1, exp) % MOD
            ans = (ans + ways) % MOD

        return ans