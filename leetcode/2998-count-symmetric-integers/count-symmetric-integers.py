class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high +1):
            cnt = 0
            total = 0
            num = i
            half = 0
            while i > 0:
                total +=  (i%10)
                i //=10
                cnt +=1
            if cnt % 2 ==0:
                c = 0
                while (cnt/2) > c:
                    half += (num%10)
                    num //=10
                    c +=1
            if half ==total/2:
                ans +=1
        return ans

