# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        HashMap = Counter(nums)
        ans = []
        for i in HashMap:
            if HashMap[i] == 1:
                ans.append(i)
        return ans
