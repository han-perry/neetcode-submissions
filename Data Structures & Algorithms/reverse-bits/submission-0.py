class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for i in range(32):
            val *= 2
            val += (n & 1)
            n >>= 1
        return val