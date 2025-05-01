class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt =  0
        num_index = defaultdict(list)
        for index , num in enumerate(nums):
            if num in num_index:
                for ind in num_index[num]:
                    if (ind * index) % k ==0:
                        cnt +=1
            num_index[num].append(index)
        return cnt