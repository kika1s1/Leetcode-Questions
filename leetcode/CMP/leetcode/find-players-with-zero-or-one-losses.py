class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser = []
        winner = []
        ans = []
        for i, j in matches:
            winner.append(i)
            losser.append(j)
        Winner = sorted(list(set(winner)-set(losser)))
        ans.append(Winner)
        losser = Counter(losser)
        
        OnlyOne = []
        for i, j in losser.items():
            if j == 1:
                OnlyOne.append(i)
        OnlyOne.sort()
        ans.append(OnlyOne)
        return ans



        