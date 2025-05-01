class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = Counter(ransomNote)
        mag = Counter(magazine)
        for char in ransomNote:
            if char not in mag or ((char in mag) and mag[char] < rans[char]):
                return False
        return True