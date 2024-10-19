#
# @lc app=leetcode id=2607 lang=python3
#
# [2607] Make K-Subarray Sums Equal
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    '''
    In the final state, we must have arr[(i + j * k) % n] being all equal, therefore removing arr[i] and adding arr[i + k] would not change the sum
    Combining with the modulo n requirement, it means we need to equate arr[i + j * gcd(n, k)]
    Therefore we separate the numbers into k buckets. In each bucket we find the median and sum the differences
    '''
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        GCD = gcd(len(arr), k)
        result = 0
        for i in range(GCD):
            tmp = []
            for j in range(i, len(arr), GCD): tmp.append(arr[j])
            tmp.sort()
            for num in tmp: result += abs(tmp[len(tmp) // 2] - num)
        return result
        
# @lc code=end

