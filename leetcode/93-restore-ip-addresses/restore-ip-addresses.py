
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(index, ans):
            if len(ans) == 4 and index == len(s):
                result.append(".".join(ans[:]))
                return
            for i in range(1, 4):
                if index + i <= len(s):
                    part = s[index:index + i]
                    if int(part) <= 255 and (len(part) == 1 or part[0] != "0"):
                        backtrack(index + i,  ans + [part])
        
        backtrack(0,  [])
        return result
