class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        sortedVowel = []
        for i in s:
            if i in vowel:
                sortedVowel.append(i)
        sortedVowel.sort()
        listS = list(s)
        cnt = 0
        for i in range(len(listS)):
            if listS[i] in vowel:
                listS[i] = sortedVowel[cnt]
                cnt += 1
        return "".join(listS)