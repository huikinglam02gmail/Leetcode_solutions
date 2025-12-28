#
# @lc app=leetcode id=3132 lang=python3
#
# [3132] Find the Integer Added to Array II
#

# @lc code=start
from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        result = 1002
        for i in range(n - 1):
            for j in range(i + 1, n):
                p1, p2 = 0, 0
                while p1 < n and (p1 == i or p1 == j):
                    p1 += 1
                x = nums2[p2] - nums1[p1]
                while p1 < n and p2 < n - 2:
                    if p1 == i or p1 == j:
                        p1 += 1
                    elif nums1[p1] + x == nums2[p2]:
                        p1 += 1
                        p2 += 1
                    else:
                        break
                if p2 == n - 2:
                    result = min(result, x)
        return result


# @lc code=end
