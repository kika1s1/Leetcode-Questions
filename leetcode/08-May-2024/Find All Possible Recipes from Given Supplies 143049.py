# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recepies: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dct=defaultdict(lambda :[])
        indegree={}
        n=len(recepies)

        for i in recepies:
            indegree[i]=0

        for i in range(n):
            for j in ingredients[i]:
                indegree[j]=0

        for i in range(n):
            for j in ingredients[i]:
                dct[j].append(recepies[i])
                indegree[recepies[i]]+=1

        st=[]
        for i in indegree:
            if indegree[i]==0:
                st.append(i)
        flst=[]
        ans=defaultdict(lambda :[])
        while st:
            x=st.pop(0)
            for i in dct[x]:
                ans[i].append(x)
                indegree[i]-=1
                if indegree[i]==0:
                    st.append(i)
            if x in recepies:
                for k in ans[x]:
                    if k not in supplies:
                        break
                else:
                    flst.append(x)
                    supplies.append(x)

        return flst