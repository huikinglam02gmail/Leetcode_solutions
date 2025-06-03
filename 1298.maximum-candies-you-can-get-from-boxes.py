#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#

from typing import List
from collections import deque
# @lc code=start
class Solution:
    '''
    From first sight, this is a BFS problem
    Open boxes are going to be placed into the queue
    We also need a set to keep the boxes which we have access to but do not have the key
    To get the candies in box[i], we need to:
    1. Have access to box[i]'s container 
    2. Open that container
    3. Open box[i] (with key or we already have it)
    4. Get the candies and keys inside    
    '''

    
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n, dq, total, no_key_yet = len(status), deque(), 0, set()
        robbed = [False for i in range(n)]
        for box in initialBoxes:
            if status[box] == 1:
                dq.append(box)
                robbed[box] = True
            else:
                no_key_yet.add(box)
        while dq:
            box = dq.popleft()
            total += candies[box]
            for key in keys[box]:
                status[key] = 1
                if key in no_key_yet and not robbed[key]:
                    dq.append(key)
                    robbed[key] = True
                    no_key_yet.remove(key)
            for nxt in containedBoxes[box]:
                if status[nxt] == 1 and not robbed[nxt]:
                    dq.append(nxt)
                    robbed[nxt] = True
                elif status[nxt] == 0 and nxt not in no_key_yet:
                    no_key_yet.add(nxt)
        return total
            
                
# @lc code=end

