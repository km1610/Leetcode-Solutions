import math
class Solution:
    def findComplement(self, num: int) -> int:
        return num^((2**(int(math.log(num,2)+1)))-1)
