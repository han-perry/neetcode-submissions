class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start_i = 0

        for i,char in enumerate(s):
            if char in seen and seen[char] >= start_i:
                start_i = seen[char] + 1
            seen[char] = i
            longest = max(longest, i - start_i + 1)
        return longest

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seen = set()
    #     longest = 0
    #     start_i = 0

    #     for i,char in enumerate(s):
    #         while char in seen:
    #             seen.remove(s[start_i])
    #             start_i += 1
    #         seen.add(char)
    #         longest = max(longest, i - start_i + 1)
    #     return longest