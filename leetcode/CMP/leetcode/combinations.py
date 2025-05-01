class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [int(x) for x in range(1, n+1)]
        return([list(x) for x in (combinations(nums, k))])
