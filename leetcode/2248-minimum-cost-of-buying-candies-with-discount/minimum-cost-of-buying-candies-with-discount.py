class Solution:
    def minimumCost(self, costs: List[int]) -> int:
        costs.sort(reverse=True)
        return sum(costs) - sum(costs[2:len(costs):3])
       