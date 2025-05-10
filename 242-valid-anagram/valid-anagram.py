class Solution:

    def counter(self, s: str) -> dict:
        strToMap = {}
        for i in s:
            if i in strToMap:
                strToMap[i] += 1
            else:
                strToMap[i] = 1
        return strToMap

    def isAnagram(self, s: str, t: str) -> bool:
        return self.counter(s) == self.counter(t)
