# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        for i in v1[::-1]:
            if i == 0:
                v1.pop()
            else:
                break
        for i in v2[::-1]:
            if i ==0:
                v2.pop()
            else:
                break
        for i, j in zip(v1, v2):
            if i < j:
                return -1
            elif i >j:
                return 1
        if len(v1) > len(v2):
            return 1
        if len(v1) < len(v2):
            return -1
        else:
            return 0