class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = 0
        nums = 0
        banned = set(banned)
        for i in range(1,n+1):
            if i in banned:
                continue
            if s+i > maxSum:
                return nums
            s += i
            nums += 1
        return nums
