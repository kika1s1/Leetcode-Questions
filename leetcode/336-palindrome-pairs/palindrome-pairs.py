class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_index = {word:i for i, word in enumerate(words)}
        def is_plandrome(string):
            return string ==string[::-1]
        ans = []
        for index, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                if is_plandrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_index and  word_index[reversed_suffix] !=index:
                        ans.append([word_index[reversed_suffix], index])
                if j != len(word) and is_plandrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_index and word_index[reversed_prefix] !=index:
                        ans.append([index, word_index[reversed_prefix]])
        return ans