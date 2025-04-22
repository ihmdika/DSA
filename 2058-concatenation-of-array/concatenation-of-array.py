class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_2 = [0] * 2 * n
        for i in range(n):
            nums_2[i] = nums[i]
            nums_2[i+n] = nums[i]
        return nums_2