class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        table=collections.defaultdict(list)
        for i,ch in enumerate(ring):
            table[ch].append(i)
        memo={}
        return self.dfs(ring,key,table,0,0,memo)
    def dfs(self,ring,key,table,i,k,memo):
        if (i,k) in memo:
            return memo[(i,k)]
        n=len(ring)
        m=len(key)
        if k>=m:
            return 0
        ans=float('inf')    
        for j in table[key[k]]:
            cost=min(abs(j-i),n-abs(j-i))
            ans=min(ans,self.dfs(ring,key,table,j,k+1,memo)+cost+1)
        memo[(i,k)]=ans
        return ans                    