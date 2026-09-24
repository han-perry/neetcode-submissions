# from string import ascii_uppercase


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        max_freq = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')

            count[idx] += 1

            max_freq = max(max_freq, count[idx])

            if r-l+1 > (k+max_freq):
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l