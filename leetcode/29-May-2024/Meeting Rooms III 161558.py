# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = list(range(n))
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start
            
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1
        
        max_booked = max(count)
        for i in range(n):
            if count[i] == max_booked:
                return i