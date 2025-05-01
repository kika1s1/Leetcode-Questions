class Solution:
    def kthCharacter(self, k: int) -> str:
        start = "a"
        while len(start) < k:
            for a in start:
                start +=chr((ord(a)% 123)+1)
        return start[k-1]
            

        