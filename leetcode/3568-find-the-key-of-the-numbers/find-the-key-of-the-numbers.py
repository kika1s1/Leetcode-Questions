class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = ""
        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)
        N = -1
        
        while True:
            if abs(N) > len(num1):
                return int(ans)
            if abs(N)>len(num2):
                return int(ans)
            if abs(N) > len(num3):
                return int(ans)
            ans =str(min(int(num1[N]), int(num2[N]), int(num3[N]))) + ans
            N -=1
        
            
            


