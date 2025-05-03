class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for ch in s:
            # check if closing has a corresponding opening
            if ch in pairs:
                # return false if stack is empty while closing OR top is not equal to an opening
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
