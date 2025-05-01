class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        prev2=cost[0]
        prev1=cost[1]
        for i in range(2,n):
            temp=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=temp
        return min(prev1,prev2)    
        