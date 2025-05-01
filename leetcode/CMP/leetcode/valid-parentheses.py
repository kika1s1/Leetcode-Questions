class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matches = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if len(stack) == 0 and i in matches:
                return False
            elif i not in matches:
                stack.append(i)
            else:
                if stack[-1] == matches[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
       