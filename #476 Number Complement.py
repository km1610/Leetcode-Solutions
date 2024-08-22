class Solution:
    def findComplement(self, num: int) -> int:

        def dectobin(num):
            return bin(num)[2::]
        
        def bintodec(num):
            s = 0
            power = 0
            for i in range(1,len(num)+1):
                s+= int(num[-i])*(2**power)
                power+=1
            return s
        
        def complement(num):
            s = ''
            for i in num:
                if i=='1':
                    s+='0'
                else:
                    s+='1'
            return s

        num = dectobin(num)
        num = complement(num)
        num = bintodec(num)
        return num
