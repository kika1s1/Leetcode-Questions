class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupMap = defaultdict(list)
        ans = []
        for i in range(len(groupSizes)):
            
            groupMap[groupSizes[i]].append(i)
        for key in groupMap.keys():
            for i in range(0, len(groupMap[key]), key):
                ans.append(groupMap[key][i:i+key])
        return ans
