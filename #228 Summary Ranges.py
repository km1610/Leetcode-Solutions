class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        output = []
        i = 0
        n = len(nums)
        start = end = nums[0]
        while i<n-1:
            if nums[i+1]!=nums[i]+1:
                if start==end:
                    output.append(str(start))
                else:
                    output.append(f'{start}->{end}')
                start,end = nums[i+1],nums[i+1]
            else:
                end = nums[i+1]
            i+=1
        if start==end:
            output.append(str(start))
        else:
            output.append(f'{start}->{end}')
        return output
