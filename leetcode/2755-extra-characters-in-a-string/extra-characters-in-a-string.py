class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        @cache
        def dp(i:int,extra:int)->int:
            if i>=n:
                return extra

            min_extra=dp(i+1,extra)
            for word in dictionary:
                if s[i:].startswith(word):
                    min_extra=min(min_extra,dp(i+len(word),extra-len(word)))

            return min_extra

        return dp(0,n)            