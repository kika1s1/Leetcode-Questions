class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        maxim = float("-inf")
        l, r = 0, len(tasks)
        by = 4
        start = 0
        while  by <= r:
            sub = tasks[l:by]
            a = max(sub) +  processorTime[start]
            maxim = max(a, maxim)
            start +=1
            l +=4
            by +=4
        return maxim


