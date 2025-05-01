class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for componenet in components:
            if componenet == '..':
                if stack:
                    stack.pop()
            elif componenet and componenet != '.':
                stack.append(componenet)
        return '/' + '/'.join(stack)
        