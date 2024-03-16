class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_found = False
        less = []
        more = []
        new_nums = []

        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]>pivot:
                more.append(nums[i])
                
        c = nums.count(pivot)
        new_nums.extend(less)
        new_nums.extend([pivot for i in range(c)])
        new_nums.extend(more)

        return new_nums
