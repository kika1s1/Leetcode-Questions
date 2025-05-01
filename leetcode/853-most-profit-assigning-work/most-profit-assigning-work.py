class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        pro_dif = sorted(zip(profit, difficulty), reverse=True)
        worker = sorted(worker, reverse=True)
        ans = 0
        l, p = 0, 0
        while l < len(worker) and p < len(pro_dif):
            if pro_dif[p][1] <= worker[l]:
                ans +=pro_dif[p][0]
                l +=1
            else:
                p +=1

        return ans