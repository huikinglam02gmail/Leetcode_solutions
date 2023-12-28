#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
import bisect
from itertools import combinations
from typing import List


class Solution:
    '''
    This problem can be solved in a similar fashion as 1755. Closest Subsequence Sum. In here we have 1 <= n <= 15, so we will TLE and MLE if we brute force all the combination (30C15 = = 1.5511752 E+8)
    Instead we break off nums into 2 parts of length n (left and right), and record the possible sums if we pick k = 0 to n elements from the array.
    for length k, there would be nCk possible sums <= 15C8 = 6435
    Then for left sum of size k, we check in the rights sum of size n - k for the total sum. The target final sum should be target = sum(nums) // 2. So we sort the rightSum[k], and binary search for target - s. Then the answer is the minimum of abs(2* (rightSum[n - k][ind] + s) - S)
    '''
    def subSetSums(self, nums):
        n = len(nums)
        sums = []
        for i in range(n + 1):
            s = set()
            for comb in combinations(nums, i):
                s.add(sum(comb))
            sums.append(sorted(s))
        return sums

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left, right =  nums[:n], nums[n:]
        leftSums = self.subSetSums(left)
        rightSums = self.subSetSums(right)
        
        S = sum(nums)
        target = S // 2
        result = float("Inf")
        for i in range(n + 1):
            for s in leftSums[i]:
                ind = bisect.bisect_left(rightSums[n - i], target - s)
                if 0 <= ind < len(rightSums[n - i]): result = min(result, abs(2 * (rightSums[n - i][ind] + s) - S))
                if 0 <= ind - 1 < len(rightSums[n - i]): result = min(result, abs(2 * (rightSums[n - i][ind - 1] + s) - S))
                if 0 <= ind + 1 < len(rightSums[n - i]): result = min(result, abs(2 * (rightSums[n - i][ind + 1] + s) - S))
        return result
# @lc code=end

