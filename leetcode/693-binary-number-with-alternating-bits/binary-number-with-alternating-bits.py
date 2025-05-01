class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        stack = []
        for i in n:
            if not stack:
                stack.append(int(i))
            else:
                if stack[-1] !=int(i):
                    stack.pop()
                    stack.append(int(i))
                else:
                    return False
        return True
