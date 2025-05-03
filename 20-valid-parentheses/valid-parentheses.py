class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closings = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closings:
                if stack and stack[-1] == closings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
