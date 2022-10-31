#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#

# @lc code=start
import heapq


class Solution:
    # This is a DP problem
    # dp[i] = maximum sum of a non-empty subsequence that ends at index i
    # We look for max(dp[l]), l = 0,...,n-1
    # When arrive at index i, we can either not include anything before (0)
    # or include any of the index i - j <= k, max(dp[j]), j = i-k,..., i-1
    # To get the max, a max heap would do the job in log(k) time
    # Add nums[i] to it
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        result, heap = - float("Inf"), []
        for i, num in enumerate(nums):
            while heap and i - heap[0][1] > k:
                heapq.heappop(heap)
            maxsofar = 0
            if heap:
                maxsofar = max(maxsofar, - heap[0][0])
            result = max(result, num + maxsofar)
            heapq.heappush(heap, [- num - maxsofar, i])
        return result

# @lc code=end

