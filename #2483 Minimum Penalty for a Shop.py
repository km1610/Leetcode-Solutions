class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ly,ln,ry,rn = 0,0,customers.count('Y'),customers.count('N')
        min_pen = ln+ry
        hour = 0
        for j in range(1,len(customers)+1):
            if customers[j-1]=='Y':
                ly+=1
                ry-=1
            else:
                ln+=1
                rn-=1
            pen = ln+ry

            if pen<min_pen:
                min_pen = pen
                hour = j
        return hour
