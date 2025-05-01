class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        x = len(A)
        k = []
        
        for indx in range(x):
            max_ = max(A[:x - indx])
            max_indx = A.index(max_) + 1
            A[:max_indx] = reversed(A[:max_indx])
            k.append(max_indx)
            
            A[:x - indx] = reversed(A[:x - indx])
            k.append(x - indx)
        return k