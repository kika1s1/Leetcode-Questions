class Solution:
    def isValid(self, word: str) -> bool:
        imp = {'@', '#', '$'}
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if len(word) < 3 or any(i in imp for i in word):
            return False
        
        cnt = 0
        cnst = set()
        v = set()

        for i in word:
            if i in vowel and not v:
                cnt += 1
                v.add(i)
            elif i.isalpha() and i not in vowel and not cnst:
                cnst.add(i)
                cnt += 1

        return cnt >= 2