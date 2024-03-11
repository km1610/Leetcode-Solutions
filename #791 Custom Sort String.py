class Solution:
    def customSortString(self, order: str, s: str) -> str:
        f = {}
        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        sub = ""
        for i in order:
            if i in f:
                sub+=i*f[i]
                f[i]=0
        
        ans = sub

        for i in f:
            ans += i*f[i]

        return ans
