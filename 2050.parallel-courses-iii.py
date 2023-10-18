#
# @lc app=leetcode id=2050 lang=python3
#
# [2050] Parallel Courses III
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    This is asking for the time to complete all courses.
    But given the prerequisite relations, suppose the dp[i] = minimum time needed to complete course i
    dp[i] = time[i] + max(dp[prereq])
    We want to know max(dp + time)
    '''
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [set() for i in range(n)]
        adj = [0] * n
        for prev, next in relations:
            graph[prev - 1].add(next - 1)
            adj[next - 1] += 1
        
        dp = [0] * n
        dq = deque()
        for i in range(n):
            if adj[i] == 0:
                dq.append(i)
        while dq:
            course = dq.popleft()
            for next in graph[course]:
                dp[next] = max(dp[next], dp[course] + time[course])
                adj[next] -= 1
                if adj[next] == 0:
                    dq.append(next)
        return max([dp[i] + time[i] for i in range(n)])
# @lc code=end

