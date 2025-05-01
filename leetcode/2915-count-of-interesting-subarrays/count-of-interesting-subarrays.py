class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = 0
        prefix = 0
        freq = Counter()
        freq[0] = 1
        for num in nums:
            if num % modulo == k:
                prefix +=1
            curr_mod = prefix % modulo
            target = (curr_mod  - k + modulo ) % modulo
            cnt += freq[target]
            freq[curr_mod] +=1
        return cnt