class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = (n/2)*(2 + (n-1) * 1)
        last_div = (n//m) 
        total_div = (last_div/2)*(2*m + (last_div-1) * m)
        return int((total - (last_div/2)*(2*m + (last_div-1) * m)) - (last_div/2) * (2*m + (last_div-1) * m))