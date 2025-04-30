class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if (int(log10(num))+1)%2 == 0:
                cnt +=1
        return cnt