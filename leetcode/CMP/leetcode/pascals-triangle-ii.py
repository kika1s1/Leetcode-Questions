class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        initial = [1]
        for i in range(rowIndex):
            l, r = 0, 1
            initial.append(0)
            initial.insert(0, 0)
            while r < len(initial):
                initial[l] = initial[l] + initial[r]
                l +=1
                r +=1
            initial.pop()
        return initial




        