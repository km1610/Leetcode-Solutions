class Solution(object):
    def maxProduct(self, nums):
        if nums[0]<nums[1]:
            twoElements = [nums[0],nums[1]]
        else:
            twoElements = [nums[1],nums[0]]

        for i in range(2,len(nums)):
            if nums[i]>twoElements[0]:
                if nums[i]>twoElements[1]:
                    twoElements[0] = twoElements[1]
                    twoElements[1] = nums[i]
                else:
                    twoElements[0] = nums[i]

        return (twoElements[0]-1) * (twoElements[1]-1)
