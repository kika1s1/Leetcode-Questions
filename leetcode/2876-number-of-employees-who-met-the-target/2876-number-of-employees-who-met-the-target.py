class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for i in range(len(hours)):
            if hours[i] >=target:
                count +=1
        return count
        