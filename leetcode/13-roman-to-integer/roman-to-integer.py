class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        rom_int = {
            "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
            "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
            "CM": 900, "M": 1000
        }
        l, r = 0, 1
        while l < r < len(s):
            both = s[l]+s[r]
            if both in rom_int:
                total +=rom_int[both]
                r +=2
                l +=2
            else:
                total +=rom_int[s[l]]
                r +=1
                l +=1
        if l < len(s):
            total +=rom_int[s[l]]
        return total