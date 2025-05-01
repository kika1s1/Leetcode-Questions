class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l, r = 0, len(skill)-1
        skill.sort()
        team = skill[l] + skill[r]
        ans = 0
        while l <=r:
            if skill[l] + skill[r] == team:
                ans +=(skill[l] * skill[r])
                r -=1
                l +=1
            else:
                return -1
        return ans