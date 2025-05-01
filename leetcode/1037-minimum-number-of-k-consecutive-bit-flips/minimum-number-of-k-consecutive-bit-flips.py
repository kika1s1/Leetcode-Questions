class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        flip_count = 0
        flipped = [0] * N
        flip_operations = 0
        
        for i in range(N):
            if i >= k:
                flip_count ^= flipped[i - k]
            if nums[i] == flip_count:
                if i + k > N:
                    return -1
                flip_operations += 1
                flip_count ^= 1
                flipped[i] = 1
            
        return flip_operations
