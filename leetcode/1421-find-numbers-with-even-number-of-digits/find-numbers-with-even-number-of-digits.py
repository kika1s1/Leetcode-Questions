class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def count_digit(num):
            cnt = 0
            while num:
                num //=10
                cnt +=1
            return cnt % 2== 0
        cnt = 0
        for num in nums:
            cnt +=count_digit(num)
        return cnt