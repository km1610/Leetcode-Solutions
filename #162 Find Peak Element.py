class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l,r = 0,len(nums)-1

        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            return 1

        while l<=r:
            mid = (l+r)//2
            if mid==0:
                if l==r:
                    return l
                l+=1
            elif mid == len(nums)-1:
                if l==r:
                    return l
                r-=1
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l = mid+1
            elif nums[mid-1]>nums[mid]:
                r = mid-1

        if nums[0]>nums[-1]:
            return 0
        return len(nums)-1
