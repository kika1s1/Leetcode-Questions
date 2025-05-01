class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 == 1:
            return False
        count = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                right = num // i
                if right <= i:
                    break
                count += (i + right)
        return count == num