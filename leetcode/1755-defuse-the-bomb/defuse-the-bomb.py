class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if k == 0:
            return [0] * len(code)
        for i in range(len(code)):
            if k >  0:
                add = 0
                for a in range(i+1, i+k+1):
                    add += code[a%len(code)]
                ans.append(add)
            else:
                add = 0
                i = len(code)+i
                for b in range(i-(-1*k), i):
                    add +=code[b%len(code)]
                ans.append(add)


        return ans
