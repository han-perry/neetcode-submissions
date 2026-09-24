class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen2index = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen2index:
                return [seen2index[complement], i]
            seen2index[num] = i
        return None

        
        