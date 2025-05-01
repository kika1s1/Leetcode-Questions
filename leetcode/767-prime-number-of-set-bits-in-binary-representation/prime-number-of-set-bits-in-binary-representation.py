class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        def isPrime(n):
            if n == 1:
                return False 
            
            div = 0
            for i in range(1, n+1):
                if n % i == 0:
                    div +=1
            return True if div <= 2 else False

        for i in range(left, right + 1):
            bitCount = i.bit_count()
            if isPrime(bitCount):
                cnt +=1
        return cnt

