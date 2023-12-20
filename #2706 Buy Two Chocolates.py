class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min1 = min(prices)
        prices.remove(min1)
        min2 = min(prices)

        if min1+min2>money:
            return money
        return money-min1-min2
