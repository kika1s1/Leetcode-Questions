class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        for i in range(1, len(sentence)):
            if sentence[i-1][-1] !=sentence[i][0]:
                return False
        return sentence[-1][-1]  == sentence[0][0]