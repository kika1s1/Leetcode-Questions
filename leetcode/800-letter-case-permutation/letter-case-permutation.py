class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        
        def backtrack(index, path):
            if index == len(s):
                results.append("".join(path))
                return
            
            path.append(s[index])
            backtrack(index + 1, path)
            path.pop()
            
            if s[index].isalpha():
                path.append(s[index].swapcase())
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return results