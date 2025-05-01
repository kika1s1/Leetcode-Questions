class Solution:
    def prefixCount(self, words: List[str], prefix: str) -> int:
        cnt = 0
        for word in words:
            if word.startswith(prefix):
                cnt +=1
        return cnt