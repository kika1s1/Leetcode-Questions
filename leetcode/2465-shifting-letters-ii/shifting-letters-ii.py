class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_amounts = [0] * (n + 1)
        
        for start, end, direction in shifts:
            if direction == 1:
                shift_amounts[start] += 1
                if end + 1 < n:
                    shift_amounts[end + 1] -= 1
            else:
                shift_amounts[start] -= 1
                if end + 1 < n:
                    shift_amounts[end + 1] += 1
        
        current_shift = 0
        for i in range(n):
            current_shift += shift_amounts[i]
            shift_amounts[i] = current_shift
        
        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift_amounts[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

