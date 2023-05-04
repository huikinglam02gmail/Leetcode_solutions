#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
from collections import deque


class Solution:
    '''
    Use two queues to simulate the process. We store the index in the R and D queues
    In each round, choose the one with lower index. This is the senator who gets to vote
    The other senator will get banned; append the voting senator to the back of the queue
    This process is continued until one of the queues got depleted
    Then report the name of the surviving queue    
    '''

    def predictPartyVictory(self, senate: str) -> str:
        queue_R = deque()
        queue_D = deque()
        n = len(senate)
        for i, party in enumerate(senate):
            if party == "R":
                queue_R.append(i)
            else:
                queue_D.append(i)
        while queue_R and queue_D:
            R = queue_R.popleft()
            D = queue_D.popleft()
            if R > D:
                queue_D.append(D + n)
            else:
                queue_R.append(R + n)
        if queue_R:
            return "Radiant"
        else:
            return "Dire"
# @lc code=end

