#
# @lc app=leetcode id=1687 lang=python3
#
# [1687] Delivering Boxes from Storage to Ports
#

# @lc code=start
from typing import List


class Solution:
    '''
    Break down the question into basics. If there are no limits on portsCount and maxBoxes, the number of trips is 1 (start from storage) + number of transitions in boxes[i][0] + 1 (go back to storage).
    When we put in the constraints, we are increasing the cost. We can break this problem into subproblems: if we finished box[:i] and we want to deliver box[i], we can attempt the following: choose a port j (j <= i) in which we transport boxes[j:i + 1] in one single trip. The additional cost we will add to preexisting cost is:
    1. is boxes[j][0] == boxs[j - 1][0], we add 2
    2. else, we just add 1
    Let dp(i) = minimum number of trips the ship needs to make to deliver boxes[:i] to their respective ports. We want to get dp(n). 
    We have the recursive relation: dp(i) = min(dp[j-1:i]) + 1(if boxes[j-1 - 1][0] != boxes[j][0]) else + 2 
    There is no need to scan all the j-i pairs because if we know box[j:i+ 1] does not satisfy the constraint, box[j + 1: i + 1] won't either. Instead we use the monotonic increasing queue and to make sure the smallet dp is always on the left
    '''
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        
# @lc code=end

