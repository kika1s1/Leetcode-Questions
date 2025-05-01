class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        ans = []
        items.sort()
        maxim = items[0][1]
        for data in items:
            data[1] = max(data[1], maxim)
            maxim = max(data[1], maxim)
        for querie in queries:
            left, right = 0, len(items)-1
            best = 0
            while left <= right:
                mid = (left + right)//2
                if items[mid][0] <= querie:
                    best  = max(best, items[mid][1])
                    left = mid + 1
                else:
                    right = mid -1
            ans.append(best)
        return ans
