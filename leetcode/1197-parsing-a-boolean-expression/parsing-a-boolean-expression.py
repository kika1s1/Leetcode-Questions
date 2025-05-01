class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        operand = []

        for char in expression:
            if char == '(':
                stack.append(char)  
            elif char == ')':
                while stack and stack[-1] != '(':
                    operand.append(stack.pop())
                stack.pop()  
                operator = stack.pop()  
                result = self.evaluate(operator, operand)
                stack.append(result)  
                operand = [] 
            elif char in 'tf':
                stack.append(char)  
            elif char in '!&|':
                stack.append(char)  
            elif char == ',':
                continue 
            
        return stack[0] == 't'

    def evaluate(self, operator, operands):
        if operator == '!':
            return 'f' if operands[-1] == 't' else 't'
        elif operator == '&':
            return 't' if all(op == 't' for op in operands) else 'f'
        elif operator == '|':
            return 't' if any(op == 't' for op in operands) else 'f'
        return 'f'  