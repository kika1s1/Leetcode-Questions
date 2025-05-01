from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = Counter(words)
        sorted_dict = [x[0] for x in sorted(words_dict.items(), key=lambda x:(-x[1], x[0]))]
        return sorted_dict[0:k]