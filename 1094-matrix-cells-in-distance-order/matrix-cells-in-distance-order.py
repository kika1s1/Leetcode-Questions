class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rC: int, cC: int) -> List[List[int]]:
        cord = []
        for i in range(rows):
            for j in range(cols):
                cord.append([i, j])
        def sorted_cord(cord):
            r1, c1 = cord
            return abs(r1-rC) + abs(c1-cC)
        cord.sort(key=sorted_cord)
        return cord