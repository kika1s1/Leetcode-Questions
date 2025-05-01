# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from heapq import heappush, heappop
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        task_indices = list(range(n))
        task_indices.sort(key=lambda x: (tasks[x][0], x)) 
        time = 0
        i = 0  
        heap = []  
        ans = [] 
        
        while i < n or heap:
            while i < n and tasks[task_indices[i]][0] <= time:
                task_index = task_indices[i]
                task_processing_time = tasks[task_index][1]
                heappush(heap, (task_processing_time, task_index))
                i += 1
            if heap:
                processing_time, task_index = heappop(heap)
                ans.append(task_index)
                time = max(time, tasks[task_index][0]) + processing_time
            elif i < n:
                time = tasks[task_indices[i]][0]
        
        return ans