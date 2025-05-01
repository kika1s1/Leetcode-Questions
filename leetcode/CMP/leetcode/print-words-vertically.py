class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        words = s.split()
        max_length = max(len(word) for word in words)
        result = []

        for i in range(max_length):
            column = []
            for word in words:
                if i < len(word):
                    column.append(word[i])
                else:
                    column.append(' ')
            result.append(''.join(column).rstrip())

        return result
            