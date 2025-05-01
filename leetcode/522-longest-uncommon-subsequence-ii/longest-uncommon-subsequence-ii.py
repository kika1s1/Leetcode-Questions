class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: len(x), reverse=True)
        N = len(strs)
        for i in range(N):
            find = strs[i]
            is_uncommon = True
            for j in range(N):
                if i == j:
                    continue
                l, r = 0, 0
                while l < len(find) and r < len(strs[j]):
                    if find[l] == strs[j][r]:
                        l += 1
                    r += 1
                if l == len(find):  
                    is_uncommon = False
                    break

            if is_uncommon:
                return len(find)

        return -1
