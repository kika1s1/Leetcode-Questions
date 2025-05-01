class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #tamirat
        ans = []
        rep = Counter(nums)
        checkPoint = len(nums)/3
        for i, j in rep.items():
            if j > checkPoint:
                ans.append(i)
        return ans
        