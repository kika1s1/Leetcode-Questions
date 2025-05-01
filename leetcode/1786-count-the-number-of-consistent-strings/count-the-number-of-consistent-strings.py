class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            changed = set(word)
            if len(changed - allowed) == 0:
                cnt +=1
        return cnt