class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        #BRUTE FORCE
        out = []
        for i in nums:
            s = 0
            for j in nums:
                s+= abs(i-j)
            out.append(s)
        return out

        #OPTIMIZED ANSWER
        rsum = sum(nums)
        n = len(nums)
        lsum = 0
        out = []

        for i in range(len(nums)):
            rsum -= nums[i]

            abs_rsum = abs((nums[i]*(n-(i+1))) - rsum)
            abs_lsum = abs((nums[i]*i) - lsum)   

            lsum += nums[i]

            out.append(abs_lsum+abs_rsum)  

        return out
