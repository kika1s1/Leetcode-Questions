class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells.sort()
        potions.sort()
        len_pos = len(potions)
        def search_start(key):
            best = -1
            l, r =  0, len(potions)-1
            while l <= r:
                mid = (l+r)//2
                if potions[mid] * key >=success:
                    best = mid
                    r = mid-1
                if potions[mid]*key < success:
                    l = mid +1
            return best
        ans = []
        for i in range(len(spells)):

            index = (search_start(spells[i]))
            if index == -1:
                ans.append(0)
            else:
                ans.append(len_pos-index)
            print(index)
        return  ans
        