#
# @lc app=leetcode id=1889 lang=python3
#
# [1889] Minimum Space Wasted From Packaging
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Notice in finding total waste in Example 1:
    (4-2) + (4-3) + (8-5) = 2*4 - (2 + 3) + 8 - 5
    So first sort packages. Then prepare the prefix Sum
    Then for each box in boxes, sort box. For each entry in box,  bisect_right for packages. Keep track of when was last cut. If cannot reach the end of package, return float("inf")
    '''
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        packages.sort()
        prefix = [0]
        for package in packages:
            prefix.append(prefix[-1] + package)

        result = float('inf')
        for box in boxes:
            box.sort()
            current = 0
            prev = 0
            for j in box:
                ind = bisect.bisect_right(packages, j)
                current += (ind - prev) * j - prefix[ind] + prefix[prev]
                prev = ind
            if prev == len(packages):
                result = min(result, current)
        return result % MOD if result < float("inf") else -1
# @lc code=end

