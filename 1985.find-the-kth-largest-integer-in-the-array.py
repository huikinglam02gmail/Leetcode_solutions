#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use Z fill and sort
    '''
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        n = max([len(x) for x in nums])
        for i, num in enumerate(nums):
            arr.append([num.zfill(n), i])
        arr.sort(reverse=True)
        return nums[arr[k - 1][1]]
# @lc code=end

