#
# @lc app=leetcode id=1681 lang=python3
#
# [1681] Minimum Incompatibility
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= k <= nums.length <= 16
    We can backtrack. Firstly, we should sort nums, so that the smaller numbers are first placed.
    Then we can use a list of lists to hold different numbers. The condition to obey is if the current number is must be larger than the last entry in a list. If we reach the end of the list and cannot find a spot, we return Inf
    '''
    
    def backTrack(self, i, cand, ans):
        if cand > ans:
            return ans
        elif i == self.n:
            return cand
        else:
            for j in range(self.k):
                if len(self.current[j]) < self.n // self.k + 1 and (len(self.current[j]) == 0 or self.nums[i] > self.current[j][-1]) and (j == 0 or self.current[j] != self.current[j - 1]):
                    self.current[j].append(self.nums[i])
                    if len(self.current[j]) == 1:
                        self.current[j].append(self.nums[i])
                    ans = self.backTrack(i + 1, cand + self.current[j][-1] - self.current[j][-2], ans)
                    self.current[j].pop()
                    if len(self.current[j]) == 1:
                        self.current[j].pop()
            return ans
    
    
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        self.nums = sorted(nums)
        self.n = len(self.nums)
        self.k = k
        self.current = [[] for i in range(k)]
        result = self.backTrack(0, 0, float('inf'))
        if result < float('inf'):
            return result
        else:
            return -1

# @lc code=end

