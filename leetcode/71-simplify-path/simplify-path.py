class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for direct in path:
            
            if direct == ".":
                continue
            elif direct == "..":
                if stack:
                    stack.pop() 
                
            else:
                if len(direct) == 0:
                    continue
                else:
                    stack.append(direct)
        return "/"+"/".join(stack)