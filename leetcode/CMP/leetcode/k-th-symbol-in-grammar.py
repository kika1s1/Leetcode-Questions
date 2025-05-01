class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        if k % 2 == 0:
            return 1 - self.kthGrammar(n-1, k//2)
        else:
            return self.kthGrammar(n-1, (k+1)//2)