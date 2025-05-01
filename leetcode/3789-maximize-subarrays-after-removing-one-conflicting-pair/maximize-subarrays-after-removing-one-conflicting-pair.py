import bisect
from collections import defaultdict
from typing import List

class Interval:
    __slots__ = ('a', 'b', 'idx')
    def __init__(self, a: int, b: int, idx: int):
        self.a = a  
        self.b = b 
        self.idx = idx 

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        intervals = []
        for i, (x, y) in enumerate(conflictingPairs):
            a, b = (x, y) if x < y else (y, x)
            intervals.append(Interval(a, b, i))
        intervals.sort(key=lambda inter: inter.b)
        
        total_subarrays = n * (n + 1) // 2
        
        I_total = 0 
        
        candidateImprovement = defaultdict(int)
        
        
        
        freq = defaultdict(int)
        
        active_keys = []
        
        uniqueCandidate = {}
        
        
        p = 0
        m = len(intervals)
        
        
        for j in range(1, n + 1):
            
            while p < m and intervals[p].b == j:
                a_val = intervals[p].a
                
                freq[a_val] += 1
                if freq[a_val] == 1:
                    
                    bisect.insort(active_keys, a_val)
                    uniqueCandidate[a_val] = intervals[p]
                else:
                    
                    uniqueCandidate[a_val] = None
                p += 1
            
            
            if not active_keys:
                F_j = 0
            else:
                F_j = active_keys[-1]
            
            I_total += F_j
            
            
            
            if active_keys:
                max_val = active_keys[-1]
                if freq[max_val] == 1:
                   
                    second_max = active_keys[-2] if len(active_keys) >= 2 else 0
                    
                    improvement = max_val - second_max
                    candidate = uniqueCandidate[max_val]
                    if candidate is not None:
                        candidateImprovement[candidate.idx] += improvement
        best_improvement = max(candidateImprovement.values(), default=0)
        return total_subarrays - I_total + best_improvement
