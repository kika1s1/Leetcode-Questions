class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers, uppers, banned = set(), set(), set()
        for char in word:
            if char.isupper():
                uppers.add(char.lower())
                if char.lower() not in lowers:
                    banned.add(char.lower())
            else:
                lowers.add(char)
                if char in uppers:
                    banned.add(char)
        return len(uppers - banned)        