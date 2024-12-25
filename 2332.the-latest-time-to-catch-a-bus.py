#
# @lc app=leetcode id=2332 lang=python3
#
# [2332] The Latest Time to Catch a Bus
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort buses.
    Then binary search between 2 and 10^9 + 1 to insert an extra passenger
    Then sort passengers and ask if the extra passenger can get on a bus
    '''
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        self.buses = sorted(buses)
        self.capacity = capacity
        l, r = 2, 1000000001
        while l < r:
            mid = l + (r - l) // 2
            if self.canCatchBus(passengers.copy(), mid): l = mid + 1
            else: r = mid
        ans = l - 1
        passengerSet = set(passengers)
        while ans in passengerSet: ans -= 1
        return ans

    def canCatchBus(self, passengers, extra):
        passengers.append(extra)
        passengers.sort()
        j = 0
        for bus in self.buses:
            current = 0
            while j < len(passengers) and current < self.capacity and passengers[j] <= bus:
                current += 1
                if passengers[j] == extra: return True
                j += 1
        return False

# @lc code=end

