class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_series(nums, 0, n-1), self.rob_series(nums, 1, n))
        
    def rob_series(self, nums, start, end):
        prev2, prev1 = 0, 0
        for i in range(start, end):
            x = nums[i]
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1