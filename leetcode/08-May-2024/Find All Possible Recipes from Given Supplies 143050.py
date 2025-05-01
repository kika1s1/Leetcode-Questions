# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        graph = {}
        visited = set()
        res = []

        for recipe, ing in zip(recipes, ingredients):
            graph[recipe] = ing

        def DFS(node):
            if node in visited:
                return False
            
            if node not in graph:
                return False
            
            visited.add(node)
            for ing in graph[node]:
                if ing not in supplies and not DFS(ing):
                    return False
            
            supplies.add(node)
            res.append(node)
            return True

        for rep in recipes:
            DFS(rep)

        return res