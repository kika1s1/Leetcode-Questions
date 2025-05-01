class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        rep = Counter(chars)
        for word in words:
            rep_word = Counter(word)
            l = len(word)
            pos = True
            for char in rep_word:
                if  char not in rep or rep[char] < rep_word[char]:
                    pos = False
                    break
            if pos:
                ans +=l
        return ans