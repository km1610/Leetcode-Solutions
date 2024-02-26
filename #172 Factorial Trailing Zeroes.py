class Solution:
    def trailingZeroes(self, n: int) -> int:

        def fact(n):
            if n==0:
                return 1
            return n*fact(n-1)
        
        factorial = fact(n)

        c = 0

        while factorial%10==0:
            factorial=factorial//10
            c+=1
        
        return c
