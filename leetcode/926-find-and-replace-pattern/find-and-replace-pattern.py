class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pat = defaultdict(list)
        res = []
        for i, v in enumerate(pattern):
            pat[v].append(i)
        for word in words:
            word_pat = defaultdict(list)
            for i, v in enumerate(word):
                word_pat[v].append(i)
            if list(word_pat.values()) == list(pat.values()):
                res.append(word)
        print(pat)
        return res