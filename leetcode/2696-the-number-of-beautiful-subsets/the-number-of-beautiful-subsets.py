class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start, current_subset):
            nonlocal count
            
            
            if current_subset:
                count += 1
            
            for i in range(start, len(nums)):
                can_add = True
                for num in current_subset:
                    if abs(num - nums[i]) == k:
                        can_add = False
                        break
                        
                if can_add:
                    current_subset.append(nums[i])
                    backtrack(i + 1, current_subset)
                    current_subset.pop()
        
        nums.sort() 
        count = 0
        backtrack(0, [])
        return count
        