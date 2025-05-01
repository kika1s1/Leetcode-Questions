class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for dir in logs:
            if stack and dir =="../":
                stack.pop()
            elif stack and dir =="./":
                continue
            else:
                if dir !="./" and dir !="../":
                    stack.append(dir)
        print(stack)
        return len(stack)


