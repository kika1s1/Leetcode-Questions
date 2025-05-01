class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        res = []
        while l < n:
            res.append(nums[l])
            res.append(nums[r])
            l+=1
            r+=1
        return res