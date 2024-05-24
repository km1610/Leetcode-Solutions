def gcd(a,b):
    if b == 0:
        return a
    if a<b:
        return gcd(b,a)
    r = a%b
    return gcd(b,r)

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums)==1:
            if nums[0]!=1:
                return False
            return True
        
        gcdRes = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                continue
            else:
                gcdRes = gcd(gcdRes,nums[i])
                if gcdRes==1:
                    return True
        return False
