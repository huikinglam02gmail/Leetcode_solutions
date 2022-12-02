#
# @lc app=leetcode id=1503 lang=python
#
# [1503] Last Moment Before All Ants Fall Out of a Plank
#

# @lc code=start
class Solution(object):
    # If they meet and turn back, it means they keep moving
    # then return max(left[i], n - 1 - right[j])
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        result = 0
        for num in left:
            result = max(result, num)
        for num in right:
            result = max(result, n - num)
        return result
# @lc code=end

