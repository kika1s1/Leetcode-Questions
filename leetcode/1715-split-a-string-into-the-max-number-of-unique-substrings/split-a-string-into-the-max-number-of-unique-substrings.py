class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return len(seen)
            
            max_split = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_split = max(max_split, backtrack(end, seen))
                    seen.remove(substring)
            
            return max_split
        
        return backtrack(0, set())
