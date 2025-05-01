class Solution:
    def countPoints(self, rings: str) -> int:
        lst=[]
        rgb=[]
        count=0
        for i in range(1,len(rings),2):
            rgb=[]
            if rings[i] not in lst:
                lst.append(rings[i])
                for j in range(1,len(rings),2):
                    if rings[j]==rings[i]:
                        if rings[j-1]=='R':
                            rgb.append(rings[j-1])
                        if rings[j-1]=='G':
                            rgb.append(rings[j-1])
                        if rings[j-1]=='B':
                            rgb.append(rings[j-1])
                if len(set(rgb))==3:
                    count+=1
        return count