import math
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        left_mean = (mean*(len(rolls)+n)) - sum(rolls)
        highest = math.ceil(left_mean/n)
        mod = left_mean%n
        if highest>6 or highest<1:
            return []
        if mod==0:
            return [highest]*n
        if highest==1:
            return []
        missed = [highest]*mod + [highest-1]*(n-mod)
        return missed
