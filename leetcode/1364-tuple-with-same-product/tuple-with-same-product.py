class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prods[nums[i] * nums[j]] += 1
        tot = 0
        for num in prods.values():
            tot += (num * (num - 1)) // 2
        return tot * 8