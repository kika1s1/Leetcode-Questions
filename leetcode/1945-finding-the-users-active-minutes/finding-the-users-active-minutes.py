class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        Map = defaultdict(set)
        for i, time in logs:
            Map[i].add(time)
        
        arr = [0] * k
        for count in Map.values():
            arr[len(count) - 1] += 1
        return arr