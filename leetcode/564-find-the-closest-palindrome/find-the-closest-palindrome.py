class Solution:
    def nearestPalindromic(self, n: str) -> str:
        half = n[:len(n)//2] if len(n)%2==0 else n[:len(n)//2+1]
        first = half+half[::-1] if len(n)%2==0 else half+half[:-1][::-1]
        tmp = str(int(half)-1)
        second = tmp+tmp[::-1] if len(n)%2==0 else tmp+tmp[:-1][::-1]
        tmp = str(int(half)+1)
        third = tmp+tmp[::-1] if len(n)%2==0 else tmp+tmp[:-1][::-1]
        fourth = "9"*(len(n)-1)
        fifth = "1"+"0"*max(0, len(n)-1)+"1"
        
        proposals = [first, second, third, fourth, fifth]
        min_diff = 10**10
        ans = ""
        for p in proposals:
            if p == n or p == "":
                continue
            else:
                diff = abs(int(p) - int(n))
                if diff < min_diff:
                    ans = p
                    min_diff = diff
                elif diff == min_diff and int(p)<int(ans):
                    ans = p
        return ans