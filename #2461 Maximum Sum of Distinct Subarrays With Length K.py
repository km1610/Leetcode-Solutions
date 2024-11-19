class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0 # sum of window
        max_sum = 0
        window = defaultdict(int)
        duplicates = 0

        for i in range(k):
            curr_sum += nums[i]

            window[nums[i]] += 1
            if window[nums[i]]>1:
                duplicates+=1
        if duplicates==0:
            max_sum = curr_sum
        
        for i in range(1,len(nums)-k+1):
            curr_sum -= nums[i-1]
            curr_sum += nums[i+k-1]
            
            if window[nums[i-1]]>1:
                duplicates-=1
            window[nums[i-1]] -= 1

            if window[nums[i+k-1]]>=1:
                duplicates += 1
            window[nums[i+k-1]] += 1
            
            if duplicates==0:
                max_sum = max(max_sum, curr_sum)

        return max_sum
