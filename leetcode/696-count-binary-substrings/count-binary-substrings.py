class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_len = 0
        cur_len = 1
        count = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_len += 1
            else:
                pre_len = cur_len
                cur_len = 1
                
            if pre_len >= cur_len:
                count += 1
        
        return count