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
        b1 = dectobin(a)
        b2 = dectobin(k)
        m = max(len(b1),len(b2))
        b1 = '0'*(m-len(b1)) + b1
        b2 = '0'*(m-len(b2)) + b2
        d = 0
        for i in range(m):
            if b1[i]!=b2[i]:
                d+=1
        return d
