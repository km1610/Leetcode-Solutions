def bintodec(s):
    pow = 0
    n = 0
    i=-1
    while i>=-len(s):
        n+= (2**pow)*int(s[i])
        i-=1
        pow+=1
    return n

class Solution:
    def numSteps(self, s: str) -> int:
        n = bintodec(s)
        s = 0
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                n=n+1
            s+=1
        return s
