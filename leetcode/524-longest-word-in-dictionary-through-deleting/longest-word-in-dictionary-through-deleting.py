class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        possible_answer = []
        for word in dictionary:
            l, r =  0, 0
            while l < len(s) and r < len(word):
                if s[l] == word[r]:
                    l +=1
                    r +=1
                else:
                    l +=1

            if r == len(word):
                possible_answer.append(word)
        if not possible_answer:
            return ""
        return sorted(possible_answer, key=lambda x: (-len(x), x))[0]