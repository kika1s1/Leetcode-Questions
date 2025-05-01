class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        cnt  = 0
        while tokens:
            if score == 0 and tokens[0] > power:
                return 0
            elif tokens[0] <= power:
                power -=tokens[0]
                cnt +=1
                score = max(score, cnt)
                tokens.pop(0)
            elif score >= 1 and len(tokens) >=2:
                cnt -=1
                # score = max(cnt, score) 
                power +=tokens[-1]
                tokens.pop(len(tokens)-1)
                
            else:
                break
        return score