def decTobin(n):
    s = ''
    while n>1:
        s+=str(n%2)
        n=n//2
    s+=str(n)
    return s[::-1]

class Solution:
    def hammingWeight(self, n: int) -> int:
        return decTobin(n).count('1')
