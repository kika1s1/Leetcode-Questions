class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_sum = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(1)
            else:
                if nums[i-1]%2 != nums[i]%2:
                    prefix_sum.append(prefix_sum[-1] + 1)
                else:
                    prefix_sum.append(1)
        ans = []
        for s,e in queries:
            if e-s+1 > prefix_sum[e] :
                ans.append(False)
            else:
                ans.append(True)
        return ans
