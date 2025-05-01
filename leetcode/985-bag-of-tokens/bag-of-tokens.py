class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        score = 0
        cnt  = 0
        while tokens:
            if score == 0 and tokens[0] > power:
                return 0
            elif tokens[0] <= power:
                power -=tokens[0]
                cnt +=1
                score = max(score, cnt)
                tokens.popleft()
            elif score >= 1 and len(tokens) >=2:
                cnt -=1
                score = max(cnt, score) 
                power +=tokens[-1]
                tokens.pop()
                
            else:
                break
        return score
