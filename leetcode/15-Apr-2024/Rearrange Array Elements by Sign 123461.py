# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for i in nums:
            if i< 0:
                neg.append(i)
            else:
                pos.append(i)
        for i, j in zip(pos, neg):
            ans.append(i)
            ans.append(j)
        return ans