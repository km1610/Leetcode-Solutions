class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse = s[::-1]
        insert = ""
        i,j = 0,len(s)
        while reverse[i::]!=s[:j]:
            insert += reverse[i]
            i+=1
            j-=1
            
        return insert + s
