# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
from sys import stdin
from typing import OrderedDict


input = lambda : stdin.readline().strip()

def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())

def answer():
    n = intp()
    s = []
    for _ in range(n):
        s.append(strp())

    graph = defaultdict(list)
    indegree = [0] * 26
    for i in range(n-1):
        if s[i][0] == s[i+1][0]:
            if s[i+1] in s[i]:
                return print("Impossible")
            j = 0
            m = min(len(s[i]), len(s[i+1]))
            while j < m:
                if s[i][j] != s[i+1][j]:
                    graph[s[i][j]].append(s[i+1][j])
                    indegree[ord(s[i+1][j]) - ord("a")] += 1
                    break
                j += 1
        else:
            graph[s[i][0]].append(s[i+1][0])
            indegree[ord(s[i+1][0]) - ord("a")] += 1
    
    queue = deque([chr(i + ord("a")) for i in range(len(indegree)) if indegree[i] == 0])
    ans = []
    while queue:
        char = queue.popleft()

        ans.append(char)
        for child in graph[char]:
            c = ord(child) - ord("a")
            
            indegree[c] -= 1

            if indegree[c] == 0:
                queue.append(child)
    
    if len(ans) != 26:
        return print("Impossible")
    
    print(''.join(ans))


answer()