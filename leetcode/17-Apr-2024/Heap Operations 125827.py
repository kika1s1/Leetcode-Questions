# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import *

n = int(input())
commands = []
heap = []

for _ in range(n):
    line = input().split()
    command = line[0]
    
    if command == 'insert':
        x = int(line[1])
        commands.append((command, x))
        heappush(heap, x)
    elif command == 'getMin':
        x = int(line[1])
        while heap and x > heap[0]:
            commands.append(('removeMin', 0))
            heappop(heap)
        
        if not heap or heap[0] > x:
            commands.append(('insert', x))
            heappush(heap, x)
        
        commands.append((command, x))
    else:  
        if not heap:
            commands.append(('insert', 1))
            heappush(heap, 1)
        
        commands.append((command, 0))
        heappop(heap)

print(len(commands))
for cmd, val in commands:
    print(cmd, val if cmd != 'removeMin' else "")