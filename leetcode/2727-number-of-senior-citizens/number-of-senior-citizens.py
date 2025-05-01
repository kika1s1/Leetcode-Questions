class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for i in range(len(details)):
            age = int(details[i][-4:-2])
            if age > 60:
                cnt +=1
        return cnt