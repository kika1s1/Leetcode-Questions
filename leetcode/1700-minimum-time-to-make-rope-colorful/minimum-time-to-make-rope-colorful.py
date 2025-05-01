from typing import *
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        t_c = zip(list(colors),neededTime)
        stack = []
        minim_time = 0
        for i, (j, k) in enumerate(t_c):
            if i == 0:
                stack.append((j, k))
            elif stack:
                a, b = stack[-1]
                if j == a:
                    if b > k:
                        # stack.pop()
                        # stack.append((j, k))
                        minim_time +=k
                    else:
                        stack.pop()
                        stack.append((j, k))
                        minim_time +=b
                else:
                    stack.append((j, k))
                    
                        
            else:
                stack.append((j, k))
                
        return minim_time
