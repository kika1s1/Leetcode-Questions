class Solution:
    def diffWaysToCompute(self, expression: str):
        if expression.isdigit():
            return [int(expression)]
        result = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                result += [eval(f'{l}{char}{r}') for l in left for r in right]
        return result
