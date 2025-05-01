class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd = 0
        even = 0
        binaryNum = bin(n)[2:][::-1]
        for index, bit in enumerate(binaryNum):
            if (index) % 2 == 0 and bit == "1":
                even +=1
            elif (index) % 2 == 1 and bit == "1":
                odd +=1




        return [even, odd]