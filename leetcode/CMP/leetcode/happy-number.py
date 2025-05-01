class Solution(object):
    def isHappy(self, n):
        isHappy = False
        checker = 0
        while int(n) >= 10:

            for i in str(n):

                checker += int(i)**2

            if checker == 1:
                isHappy = True
                break
            else:
                n = checker
                checker = 0

        if n == 1  or n == 7:
            return True
        return isHappy
