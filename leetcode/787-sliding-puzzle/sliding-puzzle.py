class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(cell) for row in board for cell in row)
        target = '123450'
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        def swap(state: str, i: int, j: int) -> str:
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)
        
        queue = deque([(start, start.index('0'), 0)])
        visited = set([start])
        
        while queue:
            state, zero, steps = queue.popleft()
            if state == target:
                return steps
            for n in neighbors[zero]:
                new_state = swap(state, zero, n)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, n, steps + 1))
        
        return -1
