class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        cnt = 0
        if len(s) != len(goal):
            return False
        for a, b in zip(s, goal):
            if a !=  b:
                cnt +=1
        if cnt == 0 and Counter(goal) == Counter(s) and len(Counter(goal)) != len(goal):
            return True
        elif cnt == 2 and Counter(goal) == Counter(s):
            return True
        return False