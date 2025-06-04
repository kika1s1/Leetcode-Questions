class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        maxim = len(word) - numFriends+1
        ans = ""
        N = len(word)
        for i in range(N):
            ans = max(ans, word[i:min(i+maxim,N)])
        return ans