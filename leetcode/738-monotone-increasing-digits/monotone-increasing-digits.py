class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        def check(number):
            ans = []
            while number >= 10:
                rem = number % 10
                ans.append(rem)
                number //=10
            ans.append(number)
            return ans == sorted(ans, reverse=True)
        p = 1
        while n >= 9:
            if check(n):
                return n
            else:
                n //=(10 **p)
                n *=(10 **p)
                n -=1
                p +=1