class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        idchars = \
        {
            'w': ('two', '2'),
            'u': ('four', '4'),
            'x': ('six', '6'),
            'f': ('five', '5'),
            'z': ('zero', '0'),
            'r': ('three', '3'), 
            't': ('eight', '8'),
            's': ('seven', '7'),
            'i': ('nine', '9'),
            'n': ('one', '1')
        }
        digits = []
        for ch, (word, digit) in idchars.items():
            digit_count = cnt[ch]
            digits.append(digit * digit_count)
            for c in word: cnt[c] -= digit_count
        return ''.join(sorted(digits))