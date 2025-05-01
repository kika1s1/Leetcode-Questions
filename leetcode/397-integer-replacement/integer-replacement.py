class Solution:
    def integerReplacement(self, n: int) -> int:
        min_op = 0

        while n!=1:
            if n%2 ==0:
                n /=2
            else:
                if n - 1 == 2:
                    n -=1
                elif int((n + 1) / 2) %2 == 0:
                    n += 1
                else:
                    n -=1
            min_op += 1

        return min_op