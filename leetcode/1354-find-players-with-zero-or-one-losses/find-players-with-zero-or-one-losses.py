class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        number_of_win = defaultdict(int)
        for winner, loser in matches:
            number_of_win[loser] +=1
            number_of_win[winner] +=0
        winner, loser = [], []
        for mach, los in number_of_win.items():
            if los ==1:
                loser.append(mach)
            elif los == 0:
                winner.append(mach)
        return [sorted(winner), sorted(loser)]
