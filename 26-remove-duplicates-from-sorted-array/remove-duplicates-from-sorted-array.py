class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1                           # the second pointer
        for i in range(1, len(nums)):   # staring from second elem since the first will always be in-place
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        
        return j