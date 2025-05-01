class Solution(object):
    def flipAndInvertImage(self, n):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for i in n:
            i.reverse()
            ans.append(i)
        last = []
        for i in ans:
            c = []
            for j in i:
                if j == 0:
                    c.append(1)
                else:
                    c.append(0)
            last.append(c)
        return last

