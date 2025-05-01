class Solution:
    def shortestPalindrome(self, s: str) -> str:
        last = len(s)-1
        origin = s
        add = []
        cnt = 0
        while True:
            check = "".join(add) + s
            cnt +=1
            if check ==check[::-1]:
                return check
            else:
                add.append(origin[last])
                last -=1