
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()
        n = len(senate)
        
        for i in range(n):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        while rad and dir:
            if rad[0] < dir[0]:
                rad.append(n)
            else:
                dir.append(n)
            rad.popleft()
            dir.popleft()
            n += 1
        
        return "Dire" if not rad else "Radiant"