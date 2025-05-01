class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(index, curr):
            if index == len(pattern) + 1:
                return ''.join(map(str, curr))
            for num in range(1, 10):
                if num not in curr:
                    if index == 0 or (pattern[index - 1] == 'I' and curr[-1] < num) or (pattern[index - 1] == 'D' and curr[-1] > num):
                        curr.append(num)
                        result = backtrack(index + 1, curr)
                        if result:
                            return result
                        curr.pop()
            return None

        return backtrack(0, [])
