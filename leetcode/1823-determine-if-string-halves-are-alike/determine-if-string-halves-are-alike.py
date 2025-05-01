class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dict = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
                'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}
        hashF = {}
        hashS = {}
        first = s[:((len(s)//2))]
        second = s[(len(s)//2):]
        for i in first:
            if i in dict:
                if i not in hashF:
                    hashF[i] = 1
                else:
                    hashF[i] += 1
        for i in second:
            if i in dict:
                if i not in hashS:
                    hashS[i] = 1
                else:
                    hashS[i] += 1

        return sum(hashF.values()) == sum(hashS.values())