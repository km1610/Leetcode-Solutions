class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==1:
            mid = (2*(n//2)+1)
            sub = mid//2
            o = sub*(sub+1)
        else:
            mid1 = (2*(n//2)+1)
            mid2 = (2*((n-1)//2)+1)
            mid = (mid1+mid2)//2
            sub = mid//2
            o = ((sub)**2)
        return o
