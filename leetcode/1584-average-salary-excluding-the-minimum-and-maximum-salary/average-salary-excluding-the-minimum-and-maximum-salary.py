class Solution:
    def average(self, salary: List[int]) -> float:
        discard = 0
        length = len(salary)
        maxim = max(salary)
        minim = min(salary)
        totalSum = sum(salary)
        for sal in salary:
            if sal == maxim or sal == minim:
                discard +=1
                totalSum -=sal
        return totalSum/(length-discard)


        