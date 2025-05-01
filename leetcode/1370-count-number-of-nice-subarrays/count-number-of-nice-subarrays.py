class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        count = 0
        cnt[k] = 1
        nice = 0
        for i in nums:
            if i %2 ==1:
                count +=1
            nice +=cnt[count]
            cnt[k+count] +=1
        return nice