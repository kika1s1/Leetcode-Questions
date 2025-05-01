class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(map(len, words))
        matrix = [[] * len(words) for _ in range(max_length)]
        for word in s.split():
            for index in range(max_length):
                matrix[index].append(word[index] if index < len(word) else " ")
        ans = []
        for word in matrix:
            ans.append("".join(word).rstrip())
        return ans
