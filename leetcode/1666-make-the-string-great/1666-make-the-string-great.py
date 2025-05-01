class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        top = -1
        for i in s:
            if top == -1:
                stack.append(i)
                top += 1

            elif i.isupper():
                low = i.lower()

                if stack[top] == low:
                    stack.pop()
                    top -= 1
                else:
                    stack.append(i)
                    top += 1
            elif stack[top].isupper():
                low = stack[top].lower()
                if low == i:
                    stack.pop()
                    top -= 1
                else:
                    stack.append(i)
                    top += 1

            else:
                stack.append(i)
                top += 1

        return "".join(stack)