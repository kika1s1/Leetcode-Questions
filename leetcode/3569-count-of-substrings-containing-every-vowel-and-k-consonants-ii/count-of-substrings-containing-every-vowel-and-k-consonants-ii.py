class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set("aeiou")
        
        P = [0] * (n + 1)
        for i, ch in enumerate(word):
            P[i + 1] = P[i] + (0 if ch in vowels else 1)
        
        prefix_indices = defaultdict(list)
        for i, count in enumerate(P):
            prefix_indices[count].append(i)
        
        last_occ = {v: -1 for v in vowels}
        ans = 0
        
        for j in range(n):
            ch = word[j]
            if ch in vowels:
                last_occ[ch] = j
            
            min_last = min(last_occ.values())
            if min_last == -1:
                continue  
            
            target = P[j + 1] - k
            
            lst = prefix_indices.get(target, [])
            count = bisect.bisect_right(lst, min_last)
            ans += count
        
        return ans
