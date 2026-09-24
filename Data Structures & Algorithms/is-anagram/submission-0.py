def make_freqs(s: str) -> dict[str, int]:
    ret = {}
    for c in s:
        ret[c] = ret.setdefault(c, 0) + 1
    return ret

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return make_freqs(s) == make_freqs(t)
        