class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def traversal(temp, lst):
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            i = 0 
            while i <= len(lst)-1:
                while i < len(lst)-1 and lst[i] == lst[i+1]:
                    i += 1
                temp.append(lst[i])
                traversal(temp, lst[:i]+lst[i+1:])
                i += 1
                temp.pop()
        
        traversal([],nums)
        return result