class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = target[0]
        minim = prev
        for num in target[1:]:
            if num > prev:
                minim += num-prev
            prev = num
        return minim