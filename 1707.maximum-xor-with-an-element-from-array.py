#
# @lc app=leetcode id=1707 lang=python3
#
# [1707] Maximum XOR With an Element From Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    binary search for the answer for each query.
    1. Sort nums
    2. For each query, we can only search inside nums[:i], in which nums[i] > m. Mark start = 0 and stop = i
    3. Then we shrink down inside nums[:i] for each digit of binary representation of x. Starting the candidate 0, we look for if num + 2^i is inside the range. If cut > start and x & 2^i > 0, our optimal target to XOR x against with nums must be smaller than nums[cut]. We set stop to be at cut. Otherwise, if we find cut < stop (given cut <= start or x & 2^i == 0), we can then set start to be at cut and add 2^i to nums
    '''
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        result = []
        for x, m in queries:
            start, stop = 0, bisect.bisect_right(nums, m)
            num = 0
            for i in range(30, -1, -1):
                cut = bisect.bisect_left(nums, num + pow(2, i), start, stop)
                if start < cut and x & pow(2, i) > 0:
                    stop = cut
                elif cut < stop:
                    start = cut
                    num += pow(2, i)
            if start < stop:
                result.append(num ^ x)
            else:
                result.append(-1)
        return result

# @lc code=end

