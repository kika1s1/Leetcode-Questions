class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return index +1
        return -1
            