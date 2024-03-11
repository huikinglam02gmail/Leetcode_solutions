#
# @lc app=leetcode id=2059 lang=python3
#
# [2059] Minimum Operations to Convert Number
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS
    '''
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        dq = deque()
        seen = set()
        dq.append(start)
        seen.add(start)
        steps = 0
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node == goal: return steps
                if 0 <= node <= 1000:
                    for num in nums:
                        if node + num not in seen:
                            seen.add(node + num)
                            dq.append(node + num)
                        if node - num not in seen:
                            seen.add(node - num)
                            dq.append(node - num)
                        if node ^ num not in seen:
                            seen.add(node ^ num)
                            dq.append(node ^ num)
            steps += 1
        return -1
# @lc code=end

