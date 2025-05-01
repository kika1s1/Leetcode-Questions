class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        stack = []
        max_length = 0
        for line in lines:
            level = line.count('\t')
            line = line.replace('\t', '')
            while len(stack) > level:
                stack.pop()
            if stack:
                current_length = stack[-1] + len(line) + 1  
            else:
                current_length = len(line)
            if '.' in line:
                max_length = max(max_length, current_length)
            else:
                stack.append(current_length)
        return max_length
