class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = {3:small,2:medium,1:big}
        

    def addCar(self, carType: int) -> bool:
        if self.space[carType]>0:
            self.space[carType]-=1
            return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
