#
# @lc app=leetcode id=3175 lang=python3
#
# [3175] Find The First Player to win K Games in a Row
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        dq = deque(range(n))
        counts = [0] * n
        for i in range(n):
            i1 = dq.popleft()
            i2 = dq.popleft()
            if skills[i1] > skills[i2]:
                dq.appendleft(i1)
                dq.append(i2)
                counts[i1] += 1
                if counts[i1] == k: return i1
            else:
                dq.appendleft(i2)
                dq.append(i1)
                counts[i2] += 1
                if counts[i2] == k: return i2
        return dq[0]
# @lc code=end

