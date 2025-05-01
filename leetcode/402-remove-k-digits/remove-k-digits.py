class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        ans = []
        for i in num:
            while ans and k and ans[-1] > i:
                ans.pop()
                k -=1
            ans.append(i)
        while k:
            ans.pop()
            k -=1
        s = ''.join(ans).lstrip('0')
        if s == '':
            return '0'
        return s
        
        