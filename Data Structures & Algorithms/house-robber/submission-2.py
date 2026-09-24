class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        values = nums[:]
        values[1] = max(values[1], values[0])
        for i in range(2, len(nums)):
            values[i] = max(values[i-2] + values[i], values[i-1])

        return values[-1]