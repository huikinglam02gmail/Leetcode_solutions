#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    number of moves to move a 1 from i to j = abs (j - i) = i - j if i > j else j - i
    So we should record all index of all occurrence of 1, and place them on a queue. Maintain the right Sum
    Then we iterate j from left to right. Whenever we see q[0] <= j, we move element from right queue to left, and update the sum.
    '''
    def minOperations(self, boxes: str) -> List[int]:
        dq = deque()
        leftS, rightS, n, leftCount = 0, 0, len(boxes), 0
        for i, box in enumerate(boxes):
            if box == "1":
                dq.append(i)
                rightS += i
        
        result = []
        for j in range(n):
            if dq and j == dq[0]:
                leftS += dq.popleft()
                rightS -= j
                leftCount += 1
            result.append(leftCount * j - leftS + rightS - len(dq) * j)
        return result
# @lc code=end

