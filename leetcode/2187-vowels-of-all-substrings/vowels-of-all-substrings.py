class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        N = len(word)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for i, char in enumerate(word):
            if char in vowel:
                ans += (i + 1) * (N - i)
        return ans