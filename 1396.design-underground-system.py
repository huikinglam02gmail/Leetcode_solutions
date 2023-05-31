#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:
    '''
    Keep a customer hash table to use id as key, check in station and time as value
    Keep a hash table that uses start and end as keys. The value would be a list of total travel time and number of travels   
    '''
    def __init__(self):
        self.customers = {}
        self.traveltimes = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            self.customers[id] = ["", 0]
        self.customers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startname, starttime = self.customers[id]
        if (startname, stationName) not in self.traveltimes:
            self.traveltimes[(startname, stationName)] = [0, 0]
        self.traveltimes[(startname, stationName)][0] += t - starttime
        self.traveltimes[(startname, stationName)][1] += 1
        self.customers[id] =["", 0]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime, totalrides = self.traveltimes[(startStation, endStation)]
        return totaltime / totalrides


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# @lc code=end

