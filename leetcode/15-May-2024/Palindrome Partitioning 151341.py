# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def backtrack(st, path):
            if st == len(s):
                ans.append(path[:])
                return
            
            for i in range(st, len(s)):
                if s[st:i+1] == s[st:i+1][::-1]:
                    path.append(s[st:i+1])
                    backtrack(i+1, path)
                    path.pop()
        
        backtrack(0, [])
        return ans