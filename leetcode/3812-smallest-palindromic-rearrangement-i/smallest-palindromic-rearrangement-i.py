class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        ans = [""] * len(s)
        N = len(s)-1
        sorted_data = sorted(list(s))
        mid = len(s)//2
        l, r = 0, 1
        pos = 0
        while l < r and l < len(s):
            if r < len(s) and sorted_data[l] == sorted_data[r]:
                ans[pos] = sorted_data[l]
                ans[N-pos] = sorted_data[l]
                l += 2
                r += 2
                pos +=1
            else:
                ans[mid] = sorted_data[l]
                l +=1
                r +=1
        return "".join(ans)

        


        