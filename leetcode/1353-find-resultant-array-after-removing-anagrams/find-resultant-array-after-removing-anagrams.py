class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) <= 1:
            return words
        copy = words[:]
        l, r = 0, 1
        while r < len(words):
            if Counter(words[l]) == Counter(words[r]):
                words.remove(words[r])
            else:
                r +=1
                l +=1
        return words