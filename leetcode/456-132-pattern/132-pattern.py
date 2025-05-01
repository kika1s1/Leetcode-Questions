class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  
        second = float('-inf') 
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])
        
        return False
