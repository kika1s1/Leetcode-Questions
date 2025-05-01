class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(s, p, removed_indices):
            s_list = list(s) 
            for idx in removed_indices:
                s_list[idx] = None  
            i, j = 0, 0
            while i < len(s_list) and j < len(p):
                if s_list[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p) 
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2
            if isSubsequence(s, p, removable[:mid]):
                left = mid 
            else:
                right = mid - 1
        return left
