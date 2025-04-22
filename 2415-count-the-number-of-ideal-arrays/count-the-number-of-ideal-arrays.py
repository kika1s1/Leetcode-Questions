MOD = 10**9 + 7
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def get_exponents(x):
            exponents = []
            d = 2
            while d * d <= x:
                count = 0
                while x % d == 0:
                    x //= d
                    count += 1
                if count > 0:
                    exponents.append(count)
                d += 1
            if x > 1:
                exponents.append(1)
            return exponents

        total = 0
        for x in range(1, maxValue + 1):
            ways = 1
            for exp in get_exponents(x):
                ways = ways * comb(n + exp - 1, exp) % MOD
            total = (total + ways) % MOD

        return total