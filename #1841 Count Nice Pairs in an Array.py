class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        ans = 0
        MOD = (10**9)+7
        n=len(nums)
        freq = {}
        for i in range(n):
            s = (nums[i] - rev(nums[i]))
            if s in freq:
                freq[s] +=1
            else:
                freq[s]=1
        for i in freq:
            ans+=(freq[i]*(freq[i]-1))//2
        return ans%MOD
        

        return ans%MOD
