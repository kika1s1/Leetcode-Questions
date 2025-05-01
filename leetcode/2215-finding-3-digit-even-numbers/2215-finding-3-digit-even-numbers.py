class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        dic = Counter(digits) 
        for num in range(100,1000,2):
            flag = 0
            for i,j in Counter(str(num)).items():
                if dic[int(i)] < j:
                    flag = 1
            if flag == 0:
                res.append(num)
        return res