from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        ans = []
        sub = []

        for line in source:
            i = 0
            if not in_block:
                sub = []
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True
                    i += 1
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False
                    i += 1
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                elif not in_block:
                    sub.append(line[i])
                i += 1
            
            if sub and not in_block:
                ans.append("".join(sub))

        return ans
