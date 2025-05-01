class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        interchangeables = 0
        for x,y in rectangles:
            ratio = x/y
            if ratio in ratios: 
                ratios[ratio] += 1
                interchangeables+=ratios[ratio]
            else:
                ratios[ratio] = 0
                
        return interchangeables