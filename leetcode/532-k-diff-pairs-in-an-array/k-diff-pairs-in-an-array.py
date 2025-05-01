class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        num_counts = Counter(nums)
        for num in num_counts:
            if k > 0 and num + k in num_counts:
                count += 1
            elif k == 0 and num_counts[num] > 1:
                count += 1
        return count