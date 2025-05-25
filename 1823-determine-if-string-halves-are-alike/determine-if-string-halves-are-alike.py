class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "u", "o", "i", "e"}
        cnt = 0
        for char in s:
            if char.lower() in vowels:
                cnt +=1
        half = 0
        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                half +=1
        return half * 2 == cnt

        """
        "tkPAdxpMfJiltOerItiv"
        """