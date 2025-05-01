class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(index, curr, num, target):

            if index == len(num):
                return sum(curr) == target
            for i in range(index, len(num)):
                curr.append(int(num[index:i+1]))
                if backtrack(i+1, curr, num, target):
                    return True
                curr.pop()
            return False
        total = 0
        for i in range(1, n+1):
            num = i*i
            target = i
            if backtrack(0, [], str(num), target):
                total +=num
        return total
