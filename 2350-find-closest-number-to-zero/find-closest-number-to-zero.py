class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minVal = nums[0]
        for num in nums:
            if abs(num) < abs(minVal):
                minVal = num

        if minVal < 0 and abs(minVal) in nums:
            return abs(minVal)
        else:
            return minVal