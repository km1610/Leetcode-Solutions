class Solution:
    def maxScore(self, s: str) -> int:
        s = list(str(s))

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
