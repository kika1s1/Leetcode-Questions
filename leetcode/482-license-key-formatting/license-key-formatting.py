class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        cnt = 0
        for i in s[::-1]:
            if i == "-" and cnt < k:
                continue
            elif i == "-" and k == cnt:
                ans = i+ans
                cnt =0
            elif i !="_" and k == cnt:
                cnt = 1
                if i.isalpha():
                    i = i.upper()
                ans = i+ "-"+ans
            else:
                cnt +=1
                if i.isalpha():
                    i = i.upper()
                ans =i+ans
        print(ans)
        return ans.lstrip("-")
                
        
        