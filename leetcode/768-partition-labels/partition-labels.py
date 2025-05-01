class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        "a":8,
        "b":5,
        "c":7
        "ababcbaca defegde hijhklij"
         012345678 9111111 16 
         r-l + 1
         8 - 0 +  1 = 9
         15-9 + 1
         7 
        """
        ans = []
        last_index = defaultdict(int)
        for index, char in enumerate(s):
            last_index[char] = index
        start = 0
        maxim = 0
        for r, char in enumerate(s):
            maxim = max(last_index[char], maxim)
            if last_index[char] == r and r == maxim:
                ans.append(r-start +1)
                start = r + 1
       
        return ans
