class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # maximum = -1
        # for i in s:
        #     r = s.rindex(i)
        #     l = s.index(i)+1
        #     maximum = max(maximum, r-l)
       
        # return maximum
        # length = -1
        # myhash= {}
        
        # for i in range(len(s)):
            
        #     if s[i] not in myhash:
        #         myhash[s[i]] = i
        #     else:
        #         length = max(length , i- myhash.get(s[i]) -1)
                
        # return length
        indices = {}  # Dictionary to store the last index of each character
        
        maximum = -1
        for i, char in enumerate(s):
            if char in indices:
                maximum = max(maximum, i - indices[char] - 1)
            else:
                indices[char] = i
                
        return maximum