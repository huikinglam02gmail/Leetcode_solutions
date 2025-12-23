#
# @lc app=leetcode id=3164 lang=python3
#
# [3164] Find the Number of Good Pairs II
#

# @lc code=start
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1Candidates = {}
        maxNum1 = 0
        for num1 in nums1:
            if num1 % k == 0: 
                nums1Candidates[num1 // k] = nums1Candidates.get(num1 // k, 0) + 1
                maxNum1 = max(maxNum1, num1 // k)
        result = 0
        nums2Dict = {}
        for num in nums2: nums2Dict[num] = nums2Dict.get(num, 0) + 1
        for num in nums2Dict:
            for val in range(num, maxNum1 + 1, num):
                if val in nums1Candidates:
                    result += nums1Candidates[val] * nums2Dict[num]
        return result
    # @lc code=end

