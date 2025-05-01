
class Solution:
    def countPairs(self, nums: List[int]) -> int:        
        n = len(nums)
        def canBe(i,j):
            x = str(nums[i])
            y = str(nums[j])
            x_len = len(x)
            y_len = len(y)
            if x_len > y_len:
                y = '0' * (x_len - y_len) + y
            if x_len < y_len:
                x = '0' * (y_len - x_len) + x
            cnt = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    cnt += 1
            if cnt <= 2 and sorted(x) == sorted(y):
                return True
            return False

        res = 0     
        for i in range(n - 1):
            for j in range(i+1, n):
                if canBe(i,j):
                    res += 1
        return res