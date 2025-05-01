class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashTable = defaultdict(int)
        guess = list(guess)
        for d in secret:
            hashTable[d] +=1
        ans =  ["", "A", "", "B"]
        similar = 0
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                similar +=1
                hashTable[secret[i]] -=1
                guess[i] ="-1"
            i +=1
        
        ans[0] = str(similar)
        dissimilar = 0
        for d in guess:
            if d in hashTable and hashTable[d] >0:
                hashTable[d] -=1
                dissimilar +=1
        ans[2] = str(dissimilar)


        return "".join(ans)