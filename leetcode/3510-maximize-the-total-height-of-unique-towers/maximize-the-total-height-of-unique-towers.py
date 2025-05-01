class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        tot = 0
        max_height = float("inf")
        for h in maximumHeight:
            if h >= max_height:
                h = max_height - 1 
            if h > 0:
                tot += h
                max_height = h  
            else:
                return -1 
        return tot