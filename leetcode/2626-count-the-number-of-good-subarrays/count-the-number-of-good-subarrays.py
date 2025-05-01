class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        count = 0
        l, r = 0, 0
        freq = defaultdict(int)
        while l <= r and r < n:
            count -=(((freq[nums[r]]) * (freq[nums[r]]-1))//2 )
            freq[nums[r]] +=1
            count +=(((freq[nums[r]]) * (freq[nums[r]]-1 ))//2)
            if count >=k:
                while l <= r  and count >=k:
                    count -=(((freq[nums[l]]) * (freq[nums[l]]-1))//2)
                    freq[nums[l]] -=1
                    count +=(((freq[nums[l]]) * (freq[nums[l]]-1))//2)
                    l +=1
                    ans +=(n-r)
            r +=1
        return ans