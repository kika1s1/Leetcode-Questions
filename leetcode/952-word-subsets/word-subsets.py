class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        word_rep = {word:Counter(word) for word in words1}
        sub_word = {word:Counter(word) for word in words2}
        subset_rep = defaultdict(int)
        for word in sub_word:
            for char, rep in sub_word[word].items():
                subset_rep[char] = max(subset_rep[char], rep)
        for word in word_rep:
            is_true = True
            for char in subset_rep:
                if char not in word_rep[word] or word_rep[word][char] < subset_rep[char]:
                    is_true = False
                    break
            if is_true:
                ans.append(word)

        return ans

