class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = defaultdict(list)
        for u, v in enumerate(friends): 
            for f in v:
                graph[u].append(f)
        
        queue = deque([id])
        visited = {id}
        stage = 0

        curr = []
        while queue:
            if stage == level:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    curr.append(node)
                break

            for _ in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            stage += 1
        else:
            curr = []
        print(curr)
        video_count = defaultdict(int)
        for friend in curr:
            for video in watchedVideos[friend]:
                video_count[video] += 1

        result = sorted(video_count.keys(), key=lambda x: (video_count[x], x))
        return result
