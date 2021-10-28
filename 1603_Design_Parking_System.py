class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.av_space = {1:big,2:medium,3:small}
        self.current_space = {1:0, 2:0, 3:0}        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.current_space[carType] <  self.av_space[carType]:
            self.current_space[carType] += 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
