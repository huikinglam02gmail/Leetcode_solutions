#
# @lc app=leetcode id=2597 lang=python3
#
# [2597] The Number of Beautiful Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    Separate nums into different groups according to num % k
    Among different groups, we can combine eligible subsets without any issue, i.e. multiply them together will give the answer
    Inside each group, we first sort the numbers appearing and count how many times it occurs.
    Then we need to keep track of two dp numbers:
    1. dp0[i] = number of subsets which do not include a[i]
    2. dp1[i] = number of subsets which includes a[i]
    give a[i + 1], dp0[i + 1] = dp0[i] + dp1[i]
    if a[i] == a[i + 1] - k: dp1[i + 1] = dp0[i] * 2 ^ (count[j][a[i + 1]] - 1)
    else: dp1[i + 1]  = (dp0[i] + dp1[i]) * 2 ^ (count[j][a[i + 1]] - 1)
    power of 2 because subset could be include / not include each occurrence of a[i + 1]
    '''
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counts = [{} for i in range(k)]
        for num in nums: counts[num % k][num] = counts[num % k].get(num, 0) + 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 =  0, 1, 0
            for a in sorted(counts[i].keys()):
                ways = pow(2, counts[i][a]) - 1
                if prev == a - k:
                    dp0, dp1 = dp0 + dp1, dp0 * ways
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * ways
                prev = a
            res *= (dp0 + dp1)
        return res - 1
# @lc code=end

