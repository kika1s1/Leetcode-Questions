class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        def is_valid(k):
            seen = set()
            count = 0
            for (x, y), ch in zip(points, s):
                if max(abs(x), abs(y)) <= k:
                    if ch in seen:
                        return False, 0  
                    seen.add(ch)
                    count += 1
            return True, count

        left = 0
        right = max(max(abs(x), abs(y)) for x, y in points)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            valid, count = is_valid(mid)
            if valid:
                best = count 
                left = mid + 1
            else:
                right = mid - 1

        return best
