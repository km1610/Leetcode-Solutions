class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        overlap = 1
        if len(self.bookings)!=0:
            for i in self.bookings:
                if (endTime<=i[1] and endTime>i[0]):
                    overlap+=1
                elif (startTime>=i[0] and endTime<=i[1]):
                    overlap+=1
                elif (startTime>=i[0] and startTime<i[1]):
                    overlap+=1
                elif (startTime<=i[0] and endTime>=i[1]):
                    overlap+=1
        if overlap==1:
            self.bookings.append([startTime,endTime])   
            return True  
              
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
