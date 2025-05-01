class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        for i in range(len(pref)):
            if i == 0:
                ans.append(pref[i])
            else:
                ans.append(pref[i] ^ pref[i-1])
        return ans