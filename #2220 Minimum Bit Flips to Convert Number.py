class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start^goal

        flips = 0

        while xor:
            flips += xor&1
            xor = xor >> 1

        return flips
