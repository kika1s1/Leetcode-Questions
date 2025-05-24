class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for index, word in enumerate(words):
            if x in word:
                ans.append(index)
        return ans