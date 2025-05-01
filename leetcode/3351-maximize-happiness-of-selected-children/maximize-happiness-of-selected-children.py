class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_happiness = nlargest(k, happiness)
        total = sum(max(0, x - i) for i, x in enumerate(max_happiness))
        return total