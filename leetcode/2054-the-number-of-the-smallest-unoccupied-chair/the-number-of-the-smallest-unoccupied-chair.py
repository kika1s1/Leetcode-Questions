class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        max_chair, heap, empty_chairs = 0, [], []
        for i in sorted(range(len(times)), key = lambda i: times[i][0]):
            while heap and heap[0][0] <= times[i][0]:
                heappush(empty_chairs, heappop(heap)[1])
            if empty_chairs:
                curr_chair = heappop(empty_chairs)
            else:
                curr_chair = max_chair
                max_chair += 1
            if i == targetFriend:
                return curr_chair
            heappush(heap, (times[i][1], curr_chair))