# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maped = defaultdict()
        for word in strs:
            sor = sorted(list(word))
            sor = "".join(sor)
            if sor not in maped:
                maped[sor] = [word]
            else:
                maped[sor].append(word)
        return (maped.values())