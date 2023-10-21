class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s = Solution().countAndSay(n-1)
        i=0
        string =''
        while i<len(s):
            count=1
            j=i+1
            while j<len(s) and s[i]==s[j]:
                j+=1
                count+=1
            string+=str(count)+s[i]
            i=j
        return string
