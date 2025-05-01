class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ('a', 'e', 'i', 'o',  'u', "A", "E", "I", "O", "U")
        ans = []
        sentence = list(sentence.split())
        for i  in range(len(sentence)):
            word = sentence[i] 
            if word[0] in vowel:
                a = "a"*(i+1)
                word +=("ma"+a)
                ans.append(word)
            else:
                a = "a"*(i+1)
                f = word[0]
                word = word[1:]+f+"ma"+a
                ans.append(word)
        return " ".join(ans)


        