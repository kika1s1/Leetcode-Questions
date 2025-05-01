class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        if len(cnt)==1:
            return len(s)
        ans = 0
        isAdded = False
        for k, v in cnt.items():
            
            if v%2 == 0:
                ans +=v
            elif v%2 ==1 and v > 2:
                ans +=(v-1)
            else:
                if not isAdded:
                    ans +=1
                    isAdded = True
        if len(s) > ans and not isAdded:
            ans +=1
        return ans
            
            