class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        while queue:
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                visited.add(node)
                if node == endGene:
                    return pos
                for gene in bank:
                    cnt = 0
                    for a, b in zip(node, gene):
                        if a!=b:
                            cnt +=1
                    if gene not in visited and cnt == 1:
                        queue.append((gene, pos+1))
                    
        return -1
