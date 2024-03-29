#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.BIG = big
        self.MEDIUM = medium
        self.SMALL = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.BIG > 0:
                self.BIG -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.MEDIUM > 0:
                self.MEDIUM -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.SMALL > 0:
                self.SMALL -= 1
                return True
            else:
                return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

