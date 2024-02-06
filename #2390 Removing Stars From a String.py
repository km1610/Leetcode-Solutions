class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        i = 0
        while i<n:
            if s[i]=="*":
                s=s[0:i-1]+s[i+1:]
                n = len(s)
                i-=2
            i+=1
        return s
