ref = ord("a")

def hash_str(s: str) -> list[int]:
    out = [0] * 26
    for c in s:
        out[ord(c) - ref] += 1
    return out


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for s in strs:
            str_counts = hash_str(s)
            seen.setdefault(tuple(str_counts), []).append(s)
        
        return list(seen.values())
