class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word1 = set(word)
        word2 = set(word.swapcase())
        print(word1 & word2)
        return len(word1 & word2)//2