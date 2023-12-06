class Solution(object):
    def totalMoney(self, n):
        moneyonMonday = 1
        saving = moneyonMonday
        day = 0
        bank = 0
        while n:
            bank+=saving
            saving+=1
            day = (day+1)%7
            if day==0:
                moneyonMonday +=1
                saving = moneyonMonday
            n-=1
        return bank
