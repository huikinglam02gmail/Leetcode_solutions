#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Typical binary search question (get yourself trained more if you don't see it!)
    We can search between 1 and sum(weights) for the possible capacities
    We see prefix sum would be handy to find the indices quick
    For example, [3,2,2,4,1,4]
    prefix = [0,3,5,7,11,12,16], for example mid = 6
    For first search we binary search (bisect_right) for 6 -> index = 3, day += 1
    second search we look for prefix[index - 1] + 6 = 11 ->  index = 5, day += 1
    third search we look for prefix[index - 1] + 6 = 17 ->  index = 8, day += 1
    Therefore we binary search until reaching len(prefix), and return the accumulated days    
    '''

    def getdays(self, capacity):
        day, i, j = 0, 0, 0
        while i < len(self.prefix):
            while j < len(self.prefix) and self.prefix[j] - self.prefix[i]<= capacity:
                j += 1
            if  j < len(self.prefix) and self.prefix[j] - self.prefix[i] > capacity:
                i = j - 1
            else:
                i = j            
            day += 1
        return day
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.prefix = [0]
        for weight in weights:
            self.prefix.append(self.prefix[-1] + weight)
        left, right = max(weights), self.prefix[-1]
        while left < right:
            mid = left + (right - left) // 2
            if self.getdays(mid) <= days:
                right = mid 
            else:
                left = mid + 1
        return left
# @lc code=end

