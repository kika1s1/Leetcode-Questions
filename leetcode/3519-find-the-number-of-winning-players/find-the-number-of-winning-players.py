class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt_repeat = defaultdict(list)
        cnt = 0
        for player, color in pick:
            cnt_repeat[player] = [0 for x in range(11)]
        
        for player, color in pick:
            cnt_repeat[player][color] +=1
        for player, color in cnt_repeat.items():
            # print(player, color)
            if player < max(color):
                cnt +=1
        
        return cnt
