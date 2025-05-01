class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        rep = {}
        for num in arr:
            rep[num] = rep.get(num-difference, 0) + 1
        print(rep) 
        return max(rep.values())
