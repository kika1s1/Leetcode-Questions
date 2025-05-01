class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = 0
        left = 0
        rep_count = Counter(nums)
        for num, rep in rep_count.items():
            pair += (rep//2)
            left +=(rep%2)
        return [pair, left]