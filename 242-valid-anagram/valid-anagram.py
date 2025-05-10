class Solution:

    def buildMap(self, s: str) -> dict:
        strToMap = {}
        for i in s:
            if i in strToMap:
                strToMap[i] += 1
            else:
                strToMap[i] = 1
        return strToMap

    def isAnagram(self, s: str, t: str) -> bool:
        return self.buildMap(s) == self.buildMap(t)
