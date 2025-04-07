#
# @lc app=leetcode id=2998 lang=python3
#
# [2998] Minimum Number of Operations to Make X and Y Equal
#

# @lc code=start
from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x: return y - x
        seen = set()
        dq = deque()
        dq.append(x)
        seen.add(x)
        steps = 0
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node == y: return steps
                if node % 11 == 0 and node // 11 not in seen:
                    dq.append(node // 11)
                    seen.add(node // 11)
                if node % 5 == 0 and node // 5 not in seen:
                    dq.append(node // 5)
                    seen.add(node // 5)
                if node - 1 not in seen:
                    dq.append(node - 1)
                    seen.add(node - 1)
                if node + 1 not in seen:
                    dq.append(node + 1)
                    seen.add(node + 1)
            steps += 1
        return -1
# @lc code=end

