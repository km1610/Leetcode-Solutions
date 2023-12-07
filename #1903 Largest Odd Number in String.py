class Solution(object):
    def largestOddNumber(self, num):
        for r in range(1,len(num)+1):
            if int(num[-r])%2==1:
                return num[:len(num)-r+1]
        return ''
        
