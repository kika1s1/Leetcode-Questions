class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num//2, num+1):
            forw = str(i)
            b = forw[::-1]
            # print(forw, b)
            if int(forw) + int(b) == num:
                return True
        return False