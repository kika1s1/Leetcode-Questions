class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in nums:
            found = False
            for group in res:
                if num in group:
                    continue
                else:
                    found = True
                    group.add(num)
                    break
            
            if not found:
                res.append(set([num]))
        
        return res
            
        

# class Solution:
#     def findMatrix(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         for i in range(len(nums)):
#             if len(ans) == 0:
#                 ans.append([nums[i]])
#                 continue
#             j = 0
#             while True:
#                 if nums[i] not in ans[j]:
#                     ans[j].append(nums[i])
#                     break

#                 j += 1
#                 if j >= len(ans):
#                     ans.append([nums[i]])
#                     break
#         return ans

