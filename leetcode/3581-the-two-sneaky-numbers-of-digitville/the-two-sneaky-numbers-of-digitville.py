class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums.count(num)==2:
                if num not in ans and len(ans) <2:
                    ans.append(num)
                
        return ans