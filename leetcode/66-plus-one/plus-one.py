class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = 0
        N = len(digits)-1
        for i in range(len(digits)):
            digit = digits[N-i] + 1
            if digit < 10:
                digits[N-i] = digit
                return digits
            else:
                digits[N-i] = 0
        digits.insert(0, 1)
        return digits


