def dtb(n):
    s = ''
    while n!=0:
        s = str(n%2) + s
        n=n//2
    return s

def btd(s):
    i,n = 1,len(s)
    num = 0
    while i<=n:
        num+=int(s[-i])*(2**(i-1))
        i+=1
    return num

class Solution:
    def reverseBits(self, n: int) -> int:
        
        s = dtb(n)
        s = '0'*(32-len(s))+s
        s = s[::-1]
        n = btd(s)
        
        return n
