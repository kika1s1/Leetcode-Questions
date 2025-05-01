class Solution:
    def countAndSay(self, n: int) -> str:
        pos = ""
        ans = "1"
        for i in range(1, n):
            pos = ""
            prev = ans[0]
            cnt = 0
            for char in ans:
                if char == prev:
                    cnt +=1
                else:
                    pos +=str(cnt)
                    pos +=prev
                    cnt = 1
                    prev = char
            pos +=str(cnt)
            pos +=prev
            ans = pos 
        return ans


        # n 
        # 1 
        # 1 1
        # 2 1
        # 1 2 1 1
        # 1 1 1 2 2 1




            
