class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        visited_a = set()
        visited_b = set()
        ans = []
        for a,b in zip(A, B):
            visited_a.add(a)
            visited_b.add(b)
            ans.append(len(visited_a & visited_b))
        return ans
