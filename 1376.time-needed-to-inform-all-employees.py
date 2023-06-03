#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    We can BFS from the head to all the leafs
    In each popped out event, we also mark the informed time for this person
    and keep tracking the max time seen    
    '''

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [set() for i in range(n)]
        for i, person in enumerate(manager):
            if person != -1:
                subordinates[person].add(i)
        dq = deque()
        dq.append([headID, 0])
        maxtime = 0
        while dq:
            person_id, time = dq.popleft()
            maxtime = max(maxtime, time)
            for subordinate in subordinates[person_id]:
                dq.append([subordinate, time + informTime[person_id]])
        return maxtime
            
# @lc code=end

