class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        pathMap = {}
        for location in paths:
            pathMap[location[0]] = location[1]
        print(pathMap)
        initial = list(pathMap.keys())
        i = 0
        
        while True:
            letInitial = initial[i]
            prev  = pathMap[letInitial] 
            check = pathMap.get(prev, 0)
            if check:

                i +=1
                prev = check
            else:
                return prev