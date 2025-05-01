from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:  
            return [-1, -1]

        
        limit = int(right ** 0.5) + 1
        base_prime = [True] * (limit + 1)
        base_prime[0] = base_prime[1] = False

        for i in range(2, limit + 1):
            if base_prime[i]:
                for j in range(i * i, limit + 1, i):
                    base_prime[j] = False

        primes = [i for i in range(2, limit + 1) if base_prime[i]]

        
        is_prime = [True] * (right - left + 1)
        if left == 1:  
            is_prime[0] = False

        for p in primes:
            start = max(p * p, (left + p - 1) // p * p)  
            for j in range(start, right + 1, p):
                is_prime[j - left] = False

        
        prime_numbers = [i for i in range(left, right + 1) if is_prime[i - left]]

       
        if len(prime_numbers) < 2:
            return [-1, -1]

        ans = [prime_numbers[0], prime_numbers[1]]
        min_diff = ans[1] - ans[0]

        for i in range(1, len(prime_numbers) - 1):
            diff = prime_numbers[i + 1] - prime_numbers[i]
            if diff < min_diff:
                min_diff = diff
                ans = [prime_numbers[i], prime_numbers[i + 1]]
                if min_diff == 2:  
                    break

        return ans
