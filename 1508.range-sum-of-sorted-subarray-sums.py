#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#

# @lc code=start
import heapq


class Solution:
#     1 <= nums[i] <= 100, subarray sums are strictly increasing
# Therefore we can start with each element first, and try to extend it
# Sum up what is between left and right
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        left -= 1
        right -= 1
        ind = 0
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, [num, i])
        result = 0
        MOD = pow(10,9) + 7
        while ind <= right:
            num, i = heapq.heappop(heap)
            if ind >= left:
                result += num
                result %= MOD
            if i < n - 1:
                heapq.heappush(heap, [nums[i+1] + num, i+1])
            ind += 1
        return result

class Solution:
# Alternatively we make use of the fact that the prefix sums are strictly increasing and conduct binary search
# Firstly, we find what exactly is S_left = sortedSubarraySum[left-1] and S_right = sortedSubarraySum[right-1] (There could be duplicates, will be taken care of later)
# Then we calculate sortedSubarrayprefixSum[S_left] and sortedSubarrayprefixSum[S_right], and return the difference

    def countSubArraySumBelowS(self, S):
        count, i = 0, 0
        for j in range(self.n + 1):
            while self.prefix[j] - self.prefix[i] > S:
                i += 1
            count += j - i
        return count
    
    def subarraySumGiveIndex(self, ind):
        l, r = 0, self.prefix[-1]
        while l < r:
            mid = (l + r) // 2
            if self.countSubArraySumBelowS(mid) < ind:
                l = mid + 1
            else:
                r = mid
        return l
    
    def sumAllSubArraysUpToIndex(self, ind):
        S = self.subarraySumGiveIndex(ind)
        result, i = 0, 0
        for j in range(self.n + 1):
            while self.prefix[j] - self.prefix[i] > S:
                i += 1
            result += self.prefix[j]*(j - i + 1) - self.prePrefix[j]
            if i > 0:
                result += self.prePrefix[i - 1]
        result -= (self.countSubArraySumBelowS(S) - ind)*S
        return result
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        self.prefix, self.prePrefix, self.n, MOD = [0], [0], n, pow(10,9) + 7
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
            self.prePrefix.append(self.prePrefix[-1] + self.prefix[-1])
        return (self.sumAllSubArraysUpToIndex(right) - self.sumAllSubArraysUpToIndex(left - 1)) % MOD
# @lc code=end

