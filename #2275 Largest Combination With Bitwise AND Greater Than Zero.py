class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_set = {}
        for i in range(32):
            bit_set[i] = 0
        
        for i in candidates:
            binary = bin(i)[2::]
            for j in range(len(binary)):
                if binary[j]=='1':
                    bit_set[len(binary) - j - 1] += 1
        max_bit_and = 0
        for i in bit_set:
            max_bit_and = max(max_bit_and, bit_set[i])

        return max_bit_and
