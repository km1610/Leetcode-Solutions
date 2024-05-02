class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        visited = set()
        m = -1
        for i in nums:
            if 0-i in visited:
                m = max(abs(i),m)
            else:
                visited.add(i)
        if m>-1:
            return m
        return -1
