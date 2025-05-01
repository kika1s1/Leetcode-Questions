class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        for elem in operations:
            if elem == 'C':
                res.pop()
            elif elem == 'D':
                double = res[-1] * 2
                res.append(double)
            elif elem == '+':
                prev2 = res[-2::]
                res.append(sum(prev2))
            else:
                res.append(int(elem))

        return sum(res)