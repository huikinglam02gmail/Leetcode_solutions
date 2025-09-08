#
# @lc app=leetcode id=3668 lang=python3
#
# [3668] Restore Finishing Order
#

# @lc code=start
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friendSet = set(friends)
        result = []
        for person in order:
            if person in friendSet:
                result.append(person)
        return result

# @lc code=end

