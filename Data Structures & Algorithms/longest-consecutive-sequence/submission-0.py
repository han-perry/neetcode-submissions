class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = frozenset(nums)
        longest = 0
        for num in nums:
            if num-1 in nums_s:
                continue
            potential = 1
            x = num
            while x+1 in nums_s:
                potential += 1
                x += 1
            longest = max(longest, potential)
        return longest
            