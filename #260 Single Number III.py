class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        lowestSetBit = xor & -xor

        res = [0, 0]
        for num in nums:
            if (lowestSetBit & num) == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res
