class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vParentheses = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for p in s:
            if p in vParentheses:
                if stack and stack[-1] == vParentheses[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack
        