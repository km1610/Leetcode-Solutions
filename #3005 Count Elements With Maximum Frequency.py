class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        m = 0

        for i in freq:
            m = max(m,freq[i])

        ans = 0

        for i in freq:
            if freq[i]==m:
                ans+=m
        
        return ans
