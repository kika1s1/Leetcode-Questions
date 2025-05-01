from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        
        def backtrack(current: str) -> str:
            if len(current) == n:
                if current not in nums_set:
                    return current
                return ""
            
            res = backtrack(current + '0')
            if res:
                return res
            
            return backtrack(current + '1')
        
        return backtrack("")
