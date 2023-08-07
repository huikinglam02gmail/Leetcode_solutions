#
# @lc app=leetcode id=1840 lang=python3
#
# [1840] Maximum Building Height
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= n <= 10^9
    0 <= restrictions.length <= min(n - 1, 10^5)
    Cannot generate the whole n building map, should check on the restrictions instead
    First, sort restrictions according to coordinates.
    Then between each restriction neighours restrictions[i]  and restrictions[i + 1], we calculate what is the buildings in between is strictly increasing in height. h = restrictions[i][1] + (restrictions[i + 1][0] - restrictions[i][0])
    if h > restrictions[i + 1][1], the maximum height a building can reach in the interval has to be trimmed down: h = restrictions[i + 1][1] + (h - restrictions[i + 1][1]) // 2
    Then we can update the result
    restriction[i + 1][1] = min(resiction[i + 1][1], h)
    Repeat the procedure left to right and then right to left.
    '''
    def scan(self):
        n = len(self.restrictions)
        result = 0
        for i in range(n - 1):
            h = self.restrictions[i][1] + abs(self.restrictions[i + 1][0] - self.restrictions[i][0])
            if h > self.restrictions[i + 1][1]:
                h = self.restrictions[i + 1][1] + (h - self.restrictions[i + 1][1]) // 2
            result = max(result, h)
            self.restrictions[i + 1][1] = min(self.restrictions[i + 1][1], h)
        return result

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        self.restrictions = restrictions
        self.restrictions.append([1, 0])
        self.restrictions.sort()
        if self.restrictions[-1][0] != n:
            self.restrictions.append([n, n - 1])   
        resultLeftToRight = self.scan()
        restrictions.reverse()
        resultRightToLeft = self.scan()
        return min(resultLeftToRight, resultRightToLeft)
# @lc code=end

