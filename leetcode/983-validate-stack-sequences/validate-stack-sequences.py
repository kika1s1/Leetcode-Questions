class Solution:
    def validateStackSequences(self, p: List[int], o: List[int]) -> bool:
        st=[]
        x=0
        for i in p:
            st.append(i)
            if len(st)>0 and st[len(st)-1]==o[x]:
                while len(st)>0 and st[len(st)-1]==o[x]:
                    x+=1
                    st.pop()
        return not st