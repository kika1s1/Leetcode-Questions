class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        N = len(intervals)
        ans = []
        start, end = intervals[0]
        for i, (s, e)in  enumerate(intervals):
            if i < N-1 and (intervals[i+1][0] <= end):
                end = max(end, intervals[i+1][1])
            elif i == N-1:
                ans.append([start, end])
            else:
                ans.append([start,end])
                start, end = intervals[i+1]
        return ans



            