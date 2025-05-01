class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # this is not topological \U0001f601
        rec_ing = defaultdict(list)
        
        for i in range(len(recipes)):
            rec_ing[recipes[i]] = ingredients[i]
        
        supplies = set(supplies)
        ans = []
        is_new_recipe_exist = True
        while is_new_recipe_exist:  
            is_new_recipe_exist = False
            for recipe in list(rec_ing.keys()):  
                can_be_made = True
                for ing in rec_ing[recipe]:  
                    if ing not in supplies:
                        can_be_made = False
                        break
                
                if can_be_made: 
                    ans.append(recipe)
                    supplies.add(recipe)
                    is_new_recipe_exist = True 
                    del rec_ing[recipe]  
            
        return ans
