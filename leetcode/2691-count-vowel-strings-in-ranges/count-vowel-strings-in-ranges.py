class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0]
        for word in words:
            if word[0] in vowels  and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        ans = []
        for s, e in queries:
            ans.append(prefix[e+1] - prefix[s])
        return ans