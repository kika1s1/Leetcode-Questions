class Solution:
    def numRabbits(self, answers):
        hashTable, total = Counter(answers), 0

        for i in hashTable:
            total += (i+1)*ceil(hashTable[i]/(i+1))
        return total 



        # cntTable = Counter(answers)
        # total =  0
        # for i in cntTable:
        #     if i == 0:
        #         total +=cntTable[i]
        #     elif i == 1:
        #         total +=(cntTable[i]+1)              
        #     else:
        #         total +=(i+1)
        # return total
        # repTable = Counter(answers)
        # ans = 0
        # for key, value in repTable.items():
        #     ans += ceil((value-1)/(key+1))
        # return ans

    

            