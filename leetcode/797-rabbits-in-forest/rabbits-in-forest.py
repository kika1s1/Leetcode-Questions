class Solution:
    def numRabbits(self, answers):
        hashTable, total = Counter(answers), 0

        for key in hashTable:
            total += (key+1)*ceil(hashTable[key]/(key+1))
        return total 

