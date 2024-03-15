class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero = nums.count(0)
        for i in nums:
            if i!=0:
                p = p*i
                
        ans = []
        for i in nums:
            if i==0:
                if zero>1:
                    ans.append(0)
                else:
                    ans.append(p)
            else:
                if zero>=1:
                    ans.append(0)
                else:
                    ans.append(p//i)        
        return ans
        
