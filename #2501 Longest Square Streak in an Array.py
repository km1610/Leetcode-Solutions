class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_l = 0
        nums = set(sorted(nums))
        visited = set()
        for x in nums:
            if x in visited:
                continue
            l = 1
            i = x
            while i*i in nums:
                visited.add(i)
                i = i*i
                l+=1
            max_l = max(max_l,l)
        if max_l>=2:
            return max_l
        return -1
