class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracets = {")" : "(", "]" : "[", "}" : "{"}

        for bracs in s:
            if bracs in bracets:
                if stack and stack[-1] == bracets[bracs]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracs)
        return True if not stack else False