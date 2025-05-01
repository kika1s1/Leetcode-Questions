class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
            if len(s) != len(goal):
                return False
            
            newS = s + s

            idx = 0
            for i in range(len(newS)):
                if newS[i] == goal[idx]:
                    idx += 1
                elif newS[i] == goal[0]:
                    idx = 1
                else:
                    idx = 0
                
                if idx == len(goal):
                    return True

            newGoal = goal + goal
            idx = 0
            for i in range(len(newGoal)):
                if newGoal[i] == s[idx]:
                    idx += 1
                elif newGoal[i] == s[0]:
                    idx = 1
                else:
                    idx = 0
                
                if idx == len(s):
                    return True

            return False