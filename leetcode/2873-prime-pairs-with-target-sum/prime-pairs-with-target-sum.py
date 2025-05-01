class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def SOE(num):
            isPrime = [True] * (num+1)
            isPrime[0] = isPrime[1] = False
            for p in range(isqrt(num)+1):
                if isPrime[p]:
                    for j in range(p*p, num+1, p):
                        isPrime[j] = False
            return isPrime

        isPrime = SOE(n)

        a = []
        for i in range(2,n//2+1):
            if isPrime[i] and isPrime[n-i]:
                a.append([i, n-i])
        return a