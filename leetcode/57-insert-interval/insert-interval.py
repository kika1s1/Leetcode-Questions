class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        start, end = newInterval
        N = len(intervals)
        for i, (s, e) in enumerate(intervals):
            if e < start:
                ans.append([s, e])
            elif s > end:
                ans.append([start, end])
                ans.extend(intervals[i:])  
                return ans
            else:
                start = min(start, s)
                end = max(end, e)
        ans.append([start, end])
        return ans
