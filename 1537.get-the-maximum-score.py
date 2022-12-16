#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#

# @lc code=start
class Solution:
    # Intuitively, we can think about the aligning nums1 and nums2
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        MOD = pow(10, 9) + 7
        current = [0, 0]
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                current[0] += nums1[p1]
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                current[1] += nums2[p2]
                p2 += 1
            else:
                currentMax = max(current)
                current = [currentMax + nums1[p1], currentMax + nums1[p1]]
                p1 += 1
                p2 += 1
        while p1 < n1:
            current[0] += nums1[p1]
            p1 += 1
        while p2 < n2:
            current[1] += nums2[p2]
            p2 += 1
        return max(current) % MOD
# @lc code=end

