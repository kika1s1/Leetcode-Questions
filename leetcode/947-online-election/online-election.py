class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winner = []
        self.times = times
        self.cnt = defaultdict(int)
        maxim = float("-inf")
        for man in persons:
            self.cnt[man] += 1
            if self.cnt[man] >= maxim:
                maxim = self.cnt[man]  
                leader = man
            self.winner.append(leader)  
    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)
        return self.winner[index-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)