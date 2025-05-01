# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known_set = set([0, firstPerson])
        
        sorted_meetings = []
        meetings.sort(key=lambda x:x[2])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)