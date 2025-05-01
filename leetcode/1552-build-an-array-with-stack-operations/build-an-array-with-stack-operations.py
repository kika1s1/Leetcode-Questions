class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []  
        cur = 1 

        for num in target:
            while cur < num:
                res.append("Push")
                res.append("Pop")
                cur += 1

            res.append("Push")
            cur += 1

        return res    