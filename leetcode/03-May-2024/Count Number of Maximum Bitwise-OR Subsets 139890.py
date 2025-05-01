# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        results = []
        
        def backtrack(nums, current, start, result):
            result.append(current[:]) 
            for i in range(start, len(nums)):
                current.append(nums[i])  
                backtrack(nums, current, i + 1, result) 
                current.pop()
        
        backtrack(nums, [], 0, results)
        
        def find_max_or(arr):
            if arr:
                p = arr[0]
                for i in range(1, len(arr)):
                    p |= arr[i]
            else:
                return 0
            return p
        
        pos_bit = []
        for i in results:
            pos_bit.append(find_max_or(i))
        
        maxim = max(pos_bit)
        return pos_bit.count(maxim)