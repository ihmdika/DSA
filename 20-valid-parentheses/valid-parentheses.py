class Solution:
    def isValid(self, s: str) -> bool:
        closings = {
            "}":"{",
            "]": "[",
            ")": "("
        }

        stack = []
        for p in s:
            if p in closings.keys():
                if stack and stack[-1] == closings[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack