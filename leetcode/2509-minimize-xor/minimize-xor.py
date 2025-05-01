class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = num2.bit_count()
        ans = 0
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) and cnt > 0:
                ans |= (1 << i)
                cnt -= 1
        for i in range(32):
            if cnt == 0:
                break
            if not (ans & (1 << i)):
                ans |= (1 << i)
                cnt -= 1
        
        return ans
