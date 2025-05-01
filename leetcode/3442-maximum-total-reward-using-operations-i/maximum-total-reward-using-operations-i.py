class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()  
        ans = {0}  
        for r in rewardValues:
            new_rewards = set()
            for x in ans:
                if r > x:
                    new_rewards.add(x + r)
            ans.update(new_rewards)
        
        return max(ans)