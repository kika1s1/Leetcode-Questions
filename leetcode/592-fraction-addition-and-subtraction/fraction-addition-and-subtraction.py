class Solution:
    def fractionAddition(self, expression: str) -> str:
        def add_fractions(n1, d1, n2, d2):
            numerator = n1 * d2 + n2 * d1
            denominator = d1 * d2
            g = gcd(abs(numerator), abs(denominator))
            return numerator // g, denominator // g
        
        i = 0
        numerator, denominator = 0, 1
        while i < len(expression):
            sign = 1
            if expression[i] in "+-":
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            j = i
            while expression[j] != '/':
                j += 1
            num = sign * int(expression[i:j])
            
            i = j + 1
            j = i
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            den = int(expression[i:j])
            
            numerator, denominator = add_fractions(numerator, denominator, num, den)
            
            i = j
        
        return f"{numerator}/{denominator}"
