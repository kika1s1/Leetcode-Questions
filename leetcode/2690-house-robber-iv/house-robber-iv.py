class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(nums,mid):
            cnt = 0
            index = None
            for i in range(len(nums)):
                if i - 1 != index and nums[i] <=mid:
                    index = i
                    cnt +=1
            return cnt >=k
        l, r = 1, max(nums)
        best = 1
        while l <=r:
            mid = (l+r)//2
            if possible(nums, mid):
                best = mid 
                r = mid-1
            else:
                l = mid +1
        return best
                