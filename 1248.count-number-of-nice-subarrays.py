#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Classic sliding window
    We also maintain a queue to hold all the indices with odd numbers
    '''

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, odd, n, result, dq = -1, 0, len(nums), 0, deque()
        for right in range(n):
            if nums[right] % 2 == 1:
                odd += 1
                dq.append(right)
            while odd > k:
                left += 1
                if nums[left] % 2 == 1:
                    odd -= 1
                    dq.popleft()
            if odd == k: result += dq[0] - left
        return result
# @lc code=end

