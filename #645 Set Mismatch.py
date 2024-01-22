class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        integer_list = set()
        ans = [0,0]
        n = len(nums)
        for i in range(n):
            if nums[i] in integer_list:
                ans[0] = nums[i]
            else:
                integer_list.add(nums[i])
                
        for i in range(1,n+1):
            if i not in integer_list:
                ans[1] = i
                break
        return ans
