#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1])/(len(salary)-2)
# @lc code=end

