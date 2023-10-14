class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            l1 = s[l+1:r]

            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            l2 = s[l+1:r]

            if len(l1)>len(longest):
                longest = l1
            if len(l2)>len(longest):
                longest = l2
        return longest
