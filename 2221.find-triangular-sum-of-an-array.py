#
# @lc app=leetcode id=2221 lang=python3
#
# [2221] Find Triangular Sum of an Array
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    1 <= nums.length <= 1000
    n ^ 2 is ok
    '''
    def triangularSum(self, nums: List[int]) -> int:
        dq = deque()
        for num in nums: dq.append(num)
        num1 = 0
        while dq:
            l = len(dq)
            num1 = dq.popleft()
            for i in range(1, l, 1):
                num2 = dq.popleft()
                dq.append((num1 + num2) % 10)
                num1 = num2
        return num1
        
# @lc code=end

