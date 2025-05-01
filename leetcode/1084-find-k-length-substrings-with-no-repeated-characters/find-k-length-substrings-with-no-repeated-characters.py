class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        substring , l = 0 , 0
        freq = Counter()
        if k > len(s) and k > 26 :
            return 0
            
        for r,char in enumerate(s) :
            freq[char] += 1
            while freq[char] > 1 or r - l + 1 > k :
                freq[s[l]] -= 1
                l += 1
            if r - l + 1 == k :
                substring += 1
        return substring   