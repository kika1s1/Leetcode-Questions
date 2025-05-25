class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        similar = False
        rep_count = Counter(words)
        cnt = 0
        for key in rep_count:
            rev  = key[::-1]
            if rev == key and rep_count[key] % 2 ==1:
                similar = True
                cnt +=(min(rep_count[rev]-1, rep_count[key]-1))
            else:
                cnt +=(min(rep_count[rev], rep_count[key]))
        return cnt * 2 + (2 if similar else 0)