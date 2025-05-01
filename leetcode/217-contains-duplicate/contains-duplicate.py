class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = set()
        for i in nums:
            if i not in value:
                value.add(i)
            else:
                return True
        return False
        # i use set because searching value in set is O(1)
        # because set is build using hashmap
        