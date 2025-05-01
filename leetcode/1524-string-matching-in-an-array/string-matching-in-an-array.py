class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for index, word in enumerate(words):
            for ind, wor in enumerate(words):
                if ind !=index and word in wor:
                    ans.append(word)
                    break
        return ans