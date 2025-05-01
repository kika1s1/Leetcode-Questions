class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace("X", "") != result.replace("X", ""):
            return False
        s_index = [(char, index) for index, char in enumerate(start) if char !="X"]
        r_index = [(char, index) for index, char in enumerate(result) if char !="X"]

        for (c1, i1), (c2, i2) in zip(s_index, r_index):
            if c1 != c2:
                return False
            if c1 == "L" and i1 < i2:
                return False
            if c1 == "R" and i1 > i2:
                return False
        return True