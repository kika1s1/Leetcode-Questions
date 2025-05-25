class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "u", "o", "i", "e"}
        cnt = 0
        half = len(s)//2
        for index, char in enumerate(s):
            if index >= half and  char.lower() in vowels:
                cnt -=1
            else:
                if  char.lower() in vowels:
                    cnt +=1
        return cnt  == 0
        # time and space 
        # O(N)  and O(1)
        """
        "tkPAdxpMfJiltOerItiv"
        """