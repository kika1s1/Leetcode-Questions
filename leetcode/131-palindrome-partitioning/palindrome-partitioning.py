
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def backtrack(start, path):
            if start == len(s):
                ans.append(path[:])
                return
            
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    path.append(s[start:i+1])
                    backtrack(i+1, path)
                    path.pop()
        
        backtrack(0, [])
        return ans