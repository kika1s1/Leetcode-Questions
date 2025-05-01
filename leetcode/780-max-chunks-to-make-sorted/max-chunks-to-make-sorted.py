class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        stack = deque()

        for i in range(n):
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)