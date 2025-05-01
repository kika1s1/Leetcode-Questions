class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hashArr = {}
        
        for i in arr:
            if i in hashArr:
                hashArr[i] +=1
            else:
                hashArr[i] =1
        return len(hashArr.values()) == len(list(set(hashArr.values())))
