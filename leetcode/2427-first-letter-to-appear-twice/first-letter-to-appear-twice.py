class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashLetter = {}
        for alp in s:
            if alp in hashLetter:
                return alp
            else:
                hashLetter[alp] = 1