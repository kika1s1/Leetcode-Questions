class Solution(object):
    def longestPalindrome(self, n):
        b = set(n)
        arr=[x for x in n]
        frq=Counter(arr)
        count=list(frq.values())
        res=0
        for i in range(len(count)):
            if count[i]%2==0:
                res+=count[i]
            else:
                res+=count[i]-1
        return res if len(arr)==res else res+1