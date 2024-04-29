def dectobin(n):
    s = ""
    while n>0:
        s = str(n%2) + s
        n=n//2
    return s

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = nums[0]
        for i in range(1,len(nums)):
            a = a^nums[i]
        b = a^k
        b = dectobin(b)
        d = 0
        for i in range(len(b)):
            if b[i]=='1':
                d+=1
        return d
