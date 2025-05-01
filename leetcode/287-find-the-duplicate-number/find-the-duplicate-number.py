class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for i, j in dict(cnt).items():
            if j >= 2:
                return i