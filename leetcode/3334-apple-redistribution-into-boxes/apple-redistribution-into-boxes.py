class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        add = 0
        for i, val in enumerate(capacity, 1):
            add +=val
            if add >=total:
                return i
        
