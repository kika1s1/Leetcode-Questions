class Solution:
    def baseNeg2(self, num: int) -> str:
        if num == 0:
            return '0'
        
        result = ''
        while num != 0:
            remainder = num % (-2)
            num //= (-2)
            
            if remainder < 0:
                remainder += 2
                num += 1
            
            result = str(remainder) + result
        return result