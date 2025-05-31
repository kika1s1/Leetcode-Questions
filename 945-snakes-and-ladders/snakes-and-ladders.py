class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        row = len(board)
        column = len(board[0])
        q = deque()
        visited = set()
        parent = [-1] * ((row * column) + 1)
        distance = [-1] * ((row * column) + 1)
        q.append(1)
        distance[1] = 0
        while q:
            node = q.popleft()

            for i in range(1, 7):
                n = node + i
                if( n >= len(parent)):
                    continue
                # snake and ladder movement
                ft = (n - 1 )// column
                r = row - 1 - ft
                c = (n - 1) % column
                if ft % 2 != 0:
                    c = column - c - 1
                
                # print(r,c)
                v = board[r][c]

                if v != -1:
                    n = v
                if n in visited or v == node:
                    continue
                
                q.append(n)
                visited.add(n)
                parent[n] = node
                distance[n] = distance[node] + 1
            
        return distance[-1]

        