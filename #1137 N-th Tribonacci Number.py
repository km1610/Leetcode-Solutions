class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        tri = [a,b,c]
        if n<3:
            return tri[n]
        for i in range(n-2):
            t=a+b+c
            a,b,c=b,c,t
        return t
