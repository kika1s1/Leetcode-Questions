class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        listWord1 = list(word1)
        for i in range(len(word2)):
            listWord1.insert(2*i+1, word2[i])
        return "".join(listWord1)
