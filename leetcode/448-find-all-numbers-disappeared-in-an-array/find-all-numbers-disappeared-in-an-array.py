class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = [int(x) for x in range(1, len(nums)+1)]
        n1 = set(nums)
        return list(set(n) - n1)


        