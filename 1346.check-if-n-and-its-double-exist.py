#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
from typing import List


class Solution:
    '''
    Separate positive, negative and zero
    If len(zero) > 1, return True
    for all negative, convert into positives
    Then keep two sets for them. Search from small to large to see if 2*x exist in the set    
    '''
    def checkIfExist(self, arr: List[int]) -> bool:
        zeros, positives, negatives = 0, set(), set()
        for num in arr:
            if num == 0: zeros += 1
            if num > 0: positives.add(num)
            if num < 0: negatives.add(-num)
        if zeros > 1: return True
        for item in positives:
            if 2 * item in positives: return True
        for item in negatives:
            if 2 * item in negatives: return True
        return False
# @lc code=end

