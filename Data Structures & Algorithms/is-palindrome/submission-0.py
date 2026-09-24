class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        i = 0
        j = n-1

        allowed = set()
        for o in range(ord("a"), ord("z") + 1):
            allowed.add(chr(o))
        for o in range(ord("0"), ord("9")+1):
            allowed.add(chr(o))
        while i < j:
            if s[i].lower() not in allowed:
                i += 1
                continue
            if s[j].lower() not in allowed:
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                print(i,s[i])
                print(j, s[j])
                return False
            i += 1
            j -= 1
        return True
