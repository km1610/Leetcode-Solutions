class Solution(object):
    def largestOddNumber(self, num):
        r = len(num)-1
        while r>=0:
            if int(num[r])%2==0:
                r-=1
            else:
                return num[0:r+1]
        return '' 
            
        
