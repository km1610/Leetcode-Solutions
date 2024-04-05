class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)==1:
            return s
        i=0
        while i<len(s)-1:
            if i<0:
                i+=1
            elif s[i].islower() and s[i+1]==s[i].upper():
                s=s[:i]+s[i+2:]
                i-=1
            elif s[i].isupper() and s[i+1]==s[i].lower():
                s=s[:i]+s[i+2:]
                i-=1
            else:
                i+=1
        return s       
