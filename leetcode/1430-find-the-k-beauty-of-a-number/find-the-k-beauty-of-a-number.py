class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        #tamirat
        num = str(num)
        cnt = 0
        for i in range(len(num)-(k-1)):
            sub = num[i:k+i]
           
            if int(sub) != 0 and  int(num) % int(sub) == 0:
                cnt +=1
        return cnt

        