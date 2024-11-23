class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        binX = bin(x)[2::]
        zero = binX.count('0')
        binN_1 = bin(n-1)[2::]
        
        if zero<len(binN_1):
            binX = '0'*(len(binN_1)-zero) + binX

        listBinX = list(binX)

        i = len(binX)-1
        j = len(binN_1)-1

        while j>=0:
            if listBinX[i] == '0':
                listBinX[i] = binN_1[j]
                j-=1
            i-=1
        
        return int(''.join(listBinX),2)
