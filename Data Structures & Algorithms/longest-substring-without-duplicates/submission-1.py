class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen_in_this_window = set() # char of sets

        l = 0
        r = 0

        for c in s:
            if c in seen_in_this_window:
                while c in seen_in_this_window:
                    stale_chr = s[l]
                    seen_in_this_window.remove(stale_chr)
                    l += 1

            seen_in_this_window.add(c)
            r += 1

            longest = max(longest, r - l)
        return longest
        
