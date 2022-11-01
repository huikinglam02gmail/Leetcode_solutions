#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        original_max = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= original_max)
        return result
# @lc code=end

