class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        alphabet = sorted(freq.keys(), reverse=True)
        result = []
        
        while alphabet:
            char = alphabet[0]  
            count = freq[char]
            
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            freq[char] -= use_count
            
            if freq[char] == 0:
                alphabet.pop(0)
            else:
                if len(alphabet) > 1:
                    next_char = alphabet[1]  
                    result.append(next_char)
                    freq[next_char] -= 1
                    
                    if freq[next_char] == 0:
                        alphabet.pop(1)
                else:
                    break
        
        return ''.join(result)
