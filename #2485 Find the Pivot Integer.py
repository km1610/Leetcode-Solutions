class Solution:
    def pivotInteger(self, n: int) -> int:
        lsum, rsum = 0, n*(n+1)//2

        for i in range(1,n+1):
            lsum+=i
            if lsum==rsum:
                return i
            rsum-=i
        
        return -1
