class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))
        s = list(str(num))
        l.sort(reverse=True)
        s1=-1
        for i in range(len(l)):
            if l[i]!=s[i]:
                s1 = l[i]
                s2 = s[i]
                ind = i
                break
        if s1==-1:
            return num
        s[ind] = s1
        for i in range(len(s)-1,-1,-1):
            if s[i]==s1:
                s[i] = s2
                break
        return int(''.join(s))
