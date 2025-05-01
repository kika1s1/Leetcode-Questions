class Solution(object):
    def calculate(self, s):
        result = 0
        number = 0
        sign = 1
        stack = []
        s = list(s)
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
            elif char == '+':
                result += number * sign
                number = 0
                sign = 1
            elif char == '-':
                result += number * sign
                number = 0
                sign = -1
        if number != 0:
            result += sign * number
        return result
