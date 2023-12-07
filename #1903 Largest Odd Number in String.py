class Solution(object):
    def largestOddNumber(self, num):
        l,r = 0,len(num)-1
        while l<=r:
            if int(num[r])%2==0:
                r-=1
            else:
                return num[l:r+1]
        return ''

            
        
