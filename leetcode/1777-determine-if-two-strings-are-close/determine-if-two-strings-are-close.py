class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_1 = collections.Counter(word1)
        count_2 = collections.Counter(word2)
        return (sorted(count_1.values()) == sorted(count_2.values()) and 
        sorted(count_1.keys()) == sorted(count_2.keys()))
        