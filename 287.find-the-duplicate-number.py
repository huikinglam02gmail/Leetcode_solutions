#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        match = False
        while not match:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if nums[slow] == nums[fast]:
                match = True
        slow = 0
        if nums[slow] != nums[fast]:
            match = False
            while not match:
                slow = nums[slow]
                fast = nums[fast]
                if nums[slow] == nums[fast]:
                    match = True
        return nums[slow]
# @lc code=end

