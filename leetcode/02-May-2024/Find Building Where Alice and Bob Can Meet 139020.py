# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        n=len(a)
        st=[]
        res=[-1]*len(q)
        q=[(q[i][0],q[i][1],i) for i in range(len(q))]
        q.sort(key=lambda x: max(x[0],x[1]))
        for i in range(n-1,-1,-1):
            while q and max(q[-1][1],q[-1][0])==i:
                x,y,pos=q.pop()
                if x>y: x,y=y,x
                if x==y or a[x]<a[y]: res[pos]=y; continue
                if len(st)==0 or st[0][0]<=a[x]: continue
                if st[-1][0]>a[x]: res[pos]=st[-1][1]; continue
                lo,hi=0,len(st)-1
                while lo<hi-1:
                    md=(lo+hi)//2
                    if st[md][0]>a[x]: lo=md
                    else: hi=md
                res[pos]=st[lo][1]
            while st:
                if a[i]>=st[-1][0]: st.pop()
                else: break
            st.append((a[i],i))
        return res