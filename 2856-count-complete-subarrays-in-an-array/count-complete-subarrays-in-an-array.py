class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        looking = Counter(set(nums))
        window = Counter()
        need = len(looking)
        N = len(nums)
        l, r = 0,0
        ans = 0
        while l <=r and r <=N-1:
            if nums[r] not in window and nums[r] in looking:
                need -=1
            window[nums[r]] +=1
            while need  == 0 and l <= r and l <=N-1:
                ans +=(N-r)
                if nums[l] in looking:
                    window[nums[l]] -=1
                    if window[nums[l]] == 0:
                        del window[nums[l]] 
                        need +=1
                l +=1
            r +=1
        return ans


            