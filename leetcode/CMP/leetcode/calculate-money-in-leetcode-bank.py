class Solution(object):
    def totalMoney(self, n):
        counter = 0
        deposit = 0
        start = 1
        increase = 0
        for i in range(n):
            if increase == 0:
                increase += 1
            counter += 1
            deposit += increase
            increase += 1
            if counter == 7:
                counter = 0
                start += 1
                increase = start

        return deposit
