class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = 0
        string = Counter(s)
        anS = Counter(t)
        for i in string:
            if i not in anS:
                cnt +=string[i]
            elif string[i] - anS[i] > 0:
                cnt += string[i] - anS[i]
            else:
                continue
        return cnt

        