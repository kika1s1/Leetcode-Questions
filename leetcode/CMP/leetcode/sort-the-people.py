class Solution(object):
    def sortPeople(self, names, heights):
        
        map = dict(zip(heights, names))
        sort = sorted(heights, reverse=True)
        ans = []

        for i in sort:
            ans.append(map[i])
        return ans