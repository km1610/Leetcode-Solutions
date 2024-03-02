class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        return nums
