import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-','+-')
        fractions = expression.split('+')
        if not fractions[0]:
            fractions.pop(0)
        split_fractions = []
        for i in fractions:
            split_fractions.append(i.split('/'))
        lcm = 1
        for i in split_fractions:
            lcm = math.lcm(lcm,int(i[1]))
        numerator = 0
        denominator = lcm
        for i in split_fractions:
            numerator += (int(i[0])*(lcm//int(i[1])))
        gcd = math.gcd(numerator,denominator)
        numerator = numerator//gcd
        denominator = denominator//gcd
        if numerator%denominator==0:
            return str(numerator) + '/1'
        return str(numerator) + '/' + str(denominator)
