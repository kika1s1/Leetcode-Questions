class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i<=len(bits)-2:
            if bits[i] == 0:
                i+=1
            else:
                i+=2
        if i == len(bits)-1:
            return True
        return False