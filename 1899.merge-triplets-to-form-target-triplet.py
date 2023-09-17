#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
from typing import List


class Solution:
    '''
    grab all the triplets that with all values smaller than target
    see if we get anything
    '''
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        satisfy = [0, 0, 0]
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                satisfy[0] = max(satisfy[0], triplets[i][0])
                satisfy[1] = max(satisfy[1], triplets[i][1])
                satisfy[2] = max(satisfy[2], triplets[i][2])
        return satisfy[0] == target[0] and satisfy[1] == target[1] and satisfy[2] == target[2]

# @lc code=end

