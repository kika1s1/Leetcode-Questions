class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {w : i for i, w in enumerate(list1)}
        c = math.inf
        res = []
        for i, w in enumerate(list2):
          if w in l1:
            if i + l1[w] < c:
              c = min(c, i+l1[w])
              res = []
              res.append(w)
            elif i + l1[w] == c:
              res.append(w)

        return res