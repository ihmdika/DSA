class Solution:
    def scoreOfString(self, s: str) -> int:
        diff = []
        for i in range(len(s) - 1):
            diff.append(abs(ord(s[i]) - ord(s[i+1])))
        return sum(diff)

