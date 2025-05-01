class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # ans = ""
        # n, m = len(word1), len(word2)
        # i, j = 0, 0
        # while i < n and j < m:
        #     ans +=word1[i]
        #     ans +=word2[j]
        #     i +=1
        #     j +=1
        # while i < n:
        #     ans +=word1[i]
        #     i +=1
        # while j < m:
        #     ans +=word2[j]
        #     j +=1
        # return ans

        
        result = ""
        n1 = len(word1)
        n2 = len(word2)
        idx1, idx2 = 0, 0
        while idx1 < n1 or idx2 < n2:
            if idx1 < n1:
                result += word1[idx1]
                idx1 += 1

            if idx2 < n2:
                result += word2[idx2]
                idx2 += 1

        return result  
