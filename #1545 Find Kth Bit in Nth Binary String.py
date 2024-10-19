class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(19):
            s = s + "1" + str(bin(int(s,2)^int("1"*len(s),2))[2::])[::-1]
        # print(s)
        return s[k-1]
