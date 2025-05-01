class Solution:
    def minSteps(self, n: int) -> int:
        min_op = 0
        div = 2
        while n > 1:
            while n % div == 0:
                min_op += div
                n //=div
            div +=1
        return min_op


