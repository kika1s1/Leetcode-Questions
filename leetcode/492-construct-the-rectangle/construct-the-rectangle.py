class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l=[area,1]
        d=l[0]-l[1]
        i=2
        x=0
        while i*i<=area:
            if area%i==0:
                x=area//i
                l=[x,i]
            i+=1
        return l
