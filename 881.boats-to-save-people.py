#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort the people. Then for each heaviest person, try to pair him with the lightest person (two-pointer)    
    '''

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result, left, right = 0, 0, len(people) - 1
        while left <= right:
            result += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return result
    # @lc code=end

