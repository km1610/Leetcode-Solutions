class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        new = []

        for i in range(0,len(nums)-2,3):
            l=[]
            if nums[i+1]-nums[i]>k or nums[i+2]-nums[i]>k:
                return []
            else:
                l = [nums[i],nums[i+1],nums[i+2]]
                new.append(l)
        return new
