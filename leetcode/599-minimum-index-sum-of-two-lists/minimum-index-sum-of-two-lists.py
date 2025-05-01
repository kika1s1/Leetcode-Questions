class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        val_index1 = {x:index for index,x in enumerate(list1) }
        val_index2 = {x:index for index,x in enumerate(list2) }
        sum_index = float("inf")
        ans = []
        for word in val_index1:
            if word in val_index2:
                if val_index1[word] + val_index2[word] < sum_index:
                    ans = []
                    ans.append(word)
                    sum_index = val_index1[word] + val_index2[word]
                elif  val_index1[word] + val_index2[word] == sum_index:
                    ans.append(word)
        return ans

