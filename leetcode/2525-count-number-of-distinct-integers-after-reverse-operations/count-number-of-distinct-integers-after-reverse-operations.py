class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        added = nums.copy()

        for i in nums:
            added.append(int(float(str(i)[::-1])))
        return len(set(added))
