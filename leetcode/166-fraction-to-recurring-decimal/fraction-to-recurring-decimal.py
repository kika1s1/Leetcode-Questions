class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: 
            return '0'
        
        result = []
        if numerator < 0 and denominator > 0 or numerator >= 0 and denominator < 0:
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        
        if remainder == 0:
            return ''.join(result)
        result.append('.')
        
        d = {}
        while remainder != 0:
            if remainder in d:
                result.insert(d[remainder], '(')
                result.append(')')
                return ''.join(result)
            
            d[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
        
        return ''.join(result)