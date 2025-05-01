class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set()
        for s, e in ranges:
            for i in range(s, e+1):
                nums.add(i)
        for i in range(left, right+1):

            if i not in nums:
                return False
        return True 