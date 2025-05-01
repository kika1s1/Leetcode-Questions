class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_arr = [0] * (rowIndex+1)
        row_arr[-1] = 1
        for _ in range(rowIndex):
            for i in range(rowIndex):
                row_arr[i] =row_arr[i] + row_arr[i+1] 
        return row_arr




