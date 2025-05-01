class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xornum(sub):
            if not sub:
                return 0
            ans = 0
            for num in sub:
                ans ^=num
            return ans
        ans = 0
        result = []
        def sub(index, curr):
            result.append(curr[:])
            for i in range(index, len(nums)):
                curr.append(nums[i])
                sub(i+1, curr)
                curr.pop()
        sub(0, [])
        for sub in result:
            ans +=xornum(sub)
        return ans
            
                
            
