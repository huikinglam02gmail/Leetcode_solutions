#
# @lc app=leetcode id=1687 lang=python3
#
# [1687] Delivering Boxes from Storage to Ports
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    '''
    Break down the question into basics. If there are no limits on maxBoxes and maxWeight, the number of trips is 1 (start from storage) + number of transitions in boxes[:][0] + 1 (go back to storage).
    When we put in the constraints, we increase the minimum cost. We can break this problem into subproblems:
    Let dp(i) = minimum number of additional trips above base line the ship needs to make to deliver boxes[:i+1] to their respective ports. (returning back to the storage port at the end). We want to get dp(n-1). 
    if we finished box[:i] and we want to deliver box[i], we can attempt the following: choose a port j (j + 1 <= i) in which we transport boxes[j + 1:i + 1] in one single trip. The additional cost we will add to the base cost is:
    1. if boxes[i][0] == boxs[i + 1][0], we add 2 (base case does not go back to storage port, we add 2 trips)
    2. else, just add 1 (as boxes[i][0] != boxes[i+1][0], instead of going directly from boxes[i][0] to boxes[i+1][0] we add 1 trip to go back to storage port)
    We have the recursive relation: dp(i) = min(dp[j:i]) + 1(if boxes[i][0] != boxes[i+1][0]) else + 2 
    There is no need to scan all the j-i pairs because if we know box[j:i+ 1] does not satisfy the constraint, box[j-1: i + 1] won't either. Instead we use the monotonic increasing queue and to make sure the smallet dp value is always on the left end
    '''
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        dq = deque()
        dq.append([-1, 1])        

        left, weight = -1, 0
        for i in range(n):
            # Add current weight and ensure the queue is fits the requirement
            weight += boxes[i][1]
            while (i - left) > maxBoxes or weight > maxWeight:
                left += 1
                weight -= boxes[left][1] 
            while dq[0][0] < left:
                dq.popleft()
            
            # The front of queue is the element that bears the minimum cost to reach there. 
            currentCost = dq[0][1] + 1
            if i < n - 1 and boxes[i][0] == boxes[i+1][0]:
                currentCost += 1
            while dq[-1][1] >= currentCost:
                dq.pop()
            dq.append([i, currentCost])
        
        # Add base cost
        for i in range(n - 1):
            if boxes[i][0] != boxes[i+1][0]:
                currentCost += 1
        return currentCost                 
        
# @lc code=end

