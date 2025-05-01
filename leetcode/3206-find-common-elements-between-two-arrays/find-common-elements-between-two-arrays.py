class Solution:
    def findIntersectionValues(self, n1: List[int], n2: List[int]) -> List[int]:
        return [sum(n in n2 for n in n1), sum(n in n1 for n in n2)]