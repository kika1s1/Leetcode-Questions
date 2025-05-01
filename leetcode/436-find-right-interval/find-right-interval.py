class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hash_index = defaultdict(int)
        for index, (start, end) in enumerate(intervals):
            hash_index[start] = index
        sorted_interval = sorted(intervals)
        N = len(sorted_interval)
        ans  = []
        def right_interval(sorted_interval, start, end):
            best = -1
            minim = float("inf")
            l, r = 0, N-1
            while l <=r:
                mid  = (l+r)//2
                s, e = sorted_interval[mid]
                if s >= end and s < minim:
                    best = hash_index[s]
                    minim = s
                    r = mid -1
                else:
                    l = mid +1
            return best
        for start, end in intervals:
            ans.append(right_interval(sorted_interval, start, end))
        return ans
