class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(str(s))
        print(s)

        n = len(s)
        zero = s.count('0')
        one = n-zero

        if zero==n or one==n:
            return n-1
        
        left = 0
        right = one
        sum = 0
        for i in range(n-1):
            if s[i]=='0':
                left+=1
            else:
                right-=1
            sum = max(sum,left+right)
        
        return sum
