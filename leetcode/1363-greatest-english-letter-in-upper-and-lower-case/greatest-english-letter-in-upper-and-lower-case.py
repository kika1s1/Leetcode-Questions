class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        chars = set(s)
        for char in chars:
            if char.isupper() and char.lower() in chars:
                # ans.append(char)
                if char > ans:
                    ans = char
        return ans