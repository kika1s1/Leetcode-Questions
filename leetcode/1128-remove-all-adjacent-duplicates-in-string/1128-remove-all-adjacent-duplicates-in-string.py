class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        top = -1
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                top += 1
            elif stack[top] == i:
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
        return "".join(stack)
