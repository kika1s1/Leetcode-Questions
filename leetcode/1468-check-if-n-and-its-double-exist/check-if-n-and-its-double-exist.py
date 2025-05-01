class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = set()
        for num in arr:
            if num*2 in visited or num/2 in visited:
                return True
            else:
                visited.add(num)
        return False