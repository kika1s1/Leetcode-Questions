class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d=deque(sorted(deck))
        res = deque()
        l = len(d)
        while l != len(res):
            t = d.pop()
            if len(res)>0:
                r = res.pop()
                res.appendleft(r)
            res.appendleft(t)
        return res