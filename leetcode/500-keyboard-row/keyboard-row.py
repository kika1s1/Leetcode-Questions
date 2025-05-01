class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = set("qwertyuiop")
        s = set("asdfghjkl")
        t = set("zxcvbnm")
        ans = []
        for word in words:
            if set(word.lower()) & f == set(word.lower()):
                ans.append(word)
            elif set(word.lower()) & s == set(word.lower()):
                ans.append(word)
            elif set(word.lower()) & t == set(word.lower()):
                ans.append(word)
        return ans
