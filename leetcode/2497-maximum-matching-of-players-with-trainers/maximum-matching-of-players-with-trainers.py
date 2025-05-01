class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        cnt = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        t = 0
        p = 0
        while t < len(trainers) and p < len(players):
            if players[p] <= trainers[t]:
                cnt +=1
                p +=1
                t +=1
            elif players[p] > trainers[t]:
                p +=1
            else:
                t +=1
        return cnt
