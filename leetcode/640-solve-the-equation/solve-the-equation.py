class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        def parse_side(side):
            x_coeff = num_sum = 0
            i = 0
            n = len(side)
            while i < n:
                sign = 1
                if side[i] == '-':
                    sign = -1
                    i += 1
                elif side[i] == '+':
                    i += 1
                num = 0
                has_number = False
                while i < n and side[i].isdigit():
                    num = num * 10 + int(side[i])
                    i += 1
                    has_number = True
                if i < n and side[i] == 'x':
                    if not has_number:
                        num = 1  
                    x_coeff += sign * num
                    i += 1  
                else:
                    num_sum += sign * num
            return x_coeff, num_sum
        left_x, left_num = parse_side(left)
        right_x, right_num = parse_side(right)
        x_total = left_x - right_x
        num_total = right_num - left_num
        if x_total == 0 and num_total == 0:
            return "Infinite solutions"
        elif x_total == 0:
            return "No solution"
        else:
            return f"x={num_total // x_total}"

