from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)

        n = len(s1)
        l = 0

        c2 = Counter()
        for r in range(len(s2)):
            c2[s2[r]] += 1

            window_size = r-l+1

            if window_size > n:
                c2[s2[l]] -= 1
                l += 1
            if c1 == c2:
                return True
        return False