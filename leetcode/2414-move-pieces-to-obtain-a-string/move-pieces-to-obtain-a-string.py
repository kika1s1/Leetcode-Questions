class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_filtered = [(c, i) for i, c in enumerate(start) if c != '_']
        target_filtered = [(c, i) for i, c in enumerate(target) if c != '_']
        
        if len(start_filtered) != len(target_filtered):
            return False
        for (c1, i1), (c2, i2) in zip(start_filtered, target_filtered):
            if c1 != c2: 
                return False
            if c1 == 'L' and i1 < i2:  
                return False
            if c1 == 'R' and i1 > i2:
                return False
        return True
