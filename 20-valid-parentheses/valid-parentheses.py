class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closings = {"}": "{", "]": "[", ")":"("}
        for e in s:
            if e in closings:
                if stack and stack[-1] == closings[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        
        return not stack