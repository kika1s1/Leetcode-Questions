class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        first = -1
        last = -1
        def isPrime(n):
            if n<2:
                return False
            for i in range(2,int(sqrt(n))+1):
                if n%i ==0:
                    return False
            return True
        for i in range(len(nums)):
            if isPrime(nums[i]):
                if first == -1:
                    first = i
                last = i
        print(first, last)
        return last - first