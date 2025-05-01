class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])

        a= b= 0
        for i in range(len(costs)//2):
            a += costs[i][0]
            b += costs[len(costs)-(i+1)][1]
        return a + b
