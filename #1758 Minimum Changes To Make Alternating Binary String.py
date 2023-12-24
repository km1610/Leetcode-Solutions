class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n%2==0:
            s1 = '10'*(n//2)
            s2 = '01'*(n//2)
        else:
            s1 = '10'*(n//2) + '1'
            s2 = '01'*(n//2) + '0'

        c1=c2=0

        for i in range(n):
            if s[i]!=s1[i]:
                c1+=1
            if s[i]!=s2[i]:
                c2+=1
        return min(c1,c2)
