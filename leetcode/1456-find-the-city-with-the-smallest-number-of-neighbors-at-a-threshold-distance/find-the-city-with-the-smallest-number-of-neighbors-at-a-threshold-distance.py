class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        def floyd_warshall():
            for i, j, w in edges:
                dist[i][j] = dist[j][i] = w

            for i in range(n):
                dist[i][i] = 0
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist
        floyd_warshall()
        num_cities = float("inf")
        city = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <=distanceThreshold:
                    cnt +=1
            if cnt <= num_cities:
                city = i
                num_cities = cnt
        return city
             
    
