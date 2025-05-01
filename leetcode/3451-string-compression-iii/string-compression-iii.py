class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1"+word[0]
        ans = []
        prev = word[0]
        cnt = 1
        for i in range(1, len(word)):
            if word[i] !=prev or cnt == 9:
                ans.append(str(cnt))
                ans.append(prev)
                prev = word[i]
                cnt = 1
                if  i == len(word)-1:
                    ans.append(str(cnt))
                    ans.append(word[i])
            elif i == len(word)-1:
                cnt +=1
                ans.append(str(cnt))
                ans.append(word[i])
            else:
                cnt +=1
        print(ans)
        return "".join(ans)
