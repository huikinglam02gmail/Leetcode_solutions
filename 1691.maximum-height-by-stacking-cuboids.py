#
# @lc app=leetcode id=1691 lang=python3
#
# [1691] Maximum Height by Stacking Cuboids 
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= n <= 100 => O(n^2) is ok.
    We are looking for maximum height, so we should first sort each cuboid, such that the largest dimension comes first. Then we sort cuboids such that they are reversely sorted.
    Then we define dp[i] = maximum height of the stacked cuboids with cuboid[i] being on top. We just need to find all previous cuboids, check if their dimensions are compatible, find the max height from it. Base case is current height
    '''
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(cuboid, reverse=True) for cuboid in cuboids]
        cuboids.sort(reverse = True)
        n = len(cuboids)
        dp = [x[0] for x in cuboids]

        result = 0
        for i in range(n):
            for j in range(i):
                if cuboids[j][0] >= cuboids[i][0] and cuboids[j][1] >= cuboids[i][1] and cuboids[j][2] >= cuboids[i][2]:
                    dp[i] = max(dp[i], cuboids[i][0] + dp[j])
            result = max(result, dp[i])
        return result
        
# @lc code=end

