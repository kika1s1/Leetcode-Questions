class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t_cnt = defaultdict(int)
        a_cnt = defaultdict(int)
        for t, a in zip(target, arr):
            t_cnt[t] +=1
            a_cnt[a] +=1
        return t_cnt == a_cnt