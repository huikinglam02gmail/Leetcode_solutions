#
# @lc app=leetcode id=1686 lang=python3
#
# [1686] Stone Game VI
#

# @lc code=start
from typing import List


class Solution:
    '''
    Suppose the final optimal playing sequence for Alice is 
    [a1, a2, ...] and the corresponding score for Bob is [b1, b2, ...]. To play optimally, this must be obeyed:
    a1 - b2 >= a2 - b1: a1 + b1 >= a2 + b2
    This tells us we should sort the numbers by a1 + b1
    '''
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        data = sorted(zip(aliceValues, bobValues), key = lambda x: - x[0] - x[1])
        alice = 0
        bob = 0
        for i, datum in enumerate(data):
            if i % 2 == 0:
                alice += datum[0]
            else:
                bob += datum[1]

        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        else:
            return -1
        
# @lc code=end

