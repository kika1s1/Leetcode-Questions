class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        digit = 1
        visited = set()
        current = 1
        while current not in visited:
            visited.add(current)
            current = ((current*10)+1)%k
            digit +=1
            if current == 0:
                return digit
        return -1