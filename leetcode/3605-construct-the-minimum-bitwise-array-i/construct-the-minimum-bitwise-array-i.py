class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            found = False
            for i in range(num):
                if i | (i + 1) == num:
                    ans.append(i)
                    found = True
                    break
            if not found:
                ans.append(-1)  
        return ans
        