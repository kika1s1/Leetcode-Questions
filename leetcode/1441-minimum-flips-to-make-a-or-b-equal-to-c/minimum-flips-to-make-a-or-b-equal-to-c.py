class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        a, b, c = a.zfill(max(len(a), len(b), len(c))), b.zfill(max(len(a), len(b), len(c))), c.zfill(max(len(a), len(b), len(c)))
        print(a, b, c)
        count = 0
        for i in range(len(a)):
            if c[i] == '1':
                if a[i] == '0' and b[i] == '0':
                    count += 1
            else:
                if a[i] == '1':
                    count += 1
                if b[i] == '1':
                    count += 1
        return count