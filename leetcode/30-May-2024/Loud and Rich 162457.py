# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def topo(node,visited,ans,value,lst):
            visited[node]=1
            for i in lst[node]:
                if visited[i]==0:
                    topo(i,visited,ans,value,lst)
                x=value[i]
                if x<value[node]:
                    value[node]=x
                    ans[node]=ans[i]
            return 

        n=len(quiet)
        visited=[0]*n
        lst=[[] for i in range(n)]
        for i,j in richer:
            lst[j].append(i)
        ans=[i for i in range(n)]
        value=[quiet[i] for i in range(n)]
        for i in range(n):
            if visited[i]==0:
                topo(i,visited,ans,value,lst)
        return ans 