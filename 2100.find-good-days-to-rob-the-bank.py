#
# @lc app=leetcode id=2100 lang=python3
#
# [2100] Find Good Days to Rob the Bank
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    We need to keep a monotonic nonincreasing queue in here, scan from left and right.
    In the first run (left -> right), we first pop left from the queue if the queue end index j if abs(i - j) > time
    Then decide if len(dq) == time
    '''
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        leftToRightOK = [False for i in range(n)]
        dq = deque()
        for i in range(n):
            if dq and abs(i - dq[0]) > time: dq.popleft()
            while dq and security[i] > security[dq[-1]]: dq.pop()
            if len(dq) == time: leftToRightOK[i] = True
            dq.append(i)
        dq = deque()
        result = []
        for i in range(n - 1, -1, -1):
            if dq and abs(i - dq[0]) > time: dq.popleft()
            while dq and security[i] > security[dq[-1]]: dq.pop()
            if len(dq) == time and leftToRightOK[i]: result.append(i)
            dq.append(i)
        return result       
# @lc code=end

