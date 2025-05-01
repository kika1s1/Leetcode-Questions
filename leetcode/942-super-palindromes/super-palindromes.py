class Solution:
    nums = set()
    for i in range(1, 10**5):
        odd = int(str(i)+str(i)[:-1][::-1])**2
        even = int(str(i)+ str(i)[::-1])**2
        if str(odd) == str(odd)[::-1]:
            nums.add(odd)
        if str(even) == str(even)[::-1]:
            nums.add(even)
    def superpalindromesInRange(self, left: str, right: str) -> int:
        cnt = 0
        for num in self.nums:
            if int(left) <=num <= int(right):
                cnt +=1
        return cnt