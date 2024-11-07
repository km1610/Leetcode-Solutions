class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bit_and = 0
        for i in range(32):
            count = 0
            for j in candidates:
                if j & (2**i):
                    count += 1
            max_bit_and = max(max_bit_and,count)
        return max_bit_and
