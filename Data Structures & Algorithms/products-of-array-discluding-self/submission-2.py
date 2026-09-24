class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])

        for j in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1] * nums[j])
        
        n = len(nums)
        ret = [suffix[n-2]] # no comprehension here for boundary cases
        for i in range(1,len(nums)-1):
            ret.append(prefix[i-1] * suffix[n-i-2])
        ret.append(prefix[-2])
        return ret