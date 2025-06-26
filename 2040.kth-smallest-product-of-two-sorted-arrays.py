#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    We are going to binary search for the solution. However, we should notice we have 6 cases:
    1. nums1[i] > 0, nums2[j] > 0, product > 0
    2. nums1[i] < 0, nums2[j] > 0, product < 0
    3. nums1[i] > 0, nums2[j] < 0, product < 0
    4. nums1[i] < 0, nums2[j] < 0, product > 0
    5. nums1[i] == 0, nums2[j] == any, product = 0
    6. nums1[i] == any, nums2[j] == 0, product = 0
    We first count the number of positive, negative and zero elements
    '''
    def countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(self, arr1, arr2, thres):
        count = 0
        j = len(arr2) - 1
        for num in arr1:
            while j >= 0 and num * arr2[j] > thres:
                j -= 1
            count += j + 1
        return count

    def countKthSmallestProductOfFourSortedPositiveArrays(self, arr1, arr2, arr3, arr4, k):
        l, r = float("inf"), - float("inf")
        if arr1 and arr2:
            l, r = arr1[0]* arr2[0], arr1[-1] * arr2[-1] + 1
        if arr3 and arr4:
            l, r = min(l, arr3[0] * arr4[0]), max(r, arr3[-1] * arr4[-1] + 1)
        while l < r:
            mid = l + (r - l) // 2
            if self.countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr1, arr2, mid) + self.countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr3, arr4, mid) < k: l = mid + 1
            else: r = mid
        return l

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1Pos, nums1Neg, nums1ZeroCount =  [], [], 0
        nums2Pos, nums2Neg, nums2ZeroCount =  [], [], 0
        for num1 in nums1:
            if num1 > 0: nums1Pos.append(num1)
            elif num1 < 0: nums1Neg.append(- num1)
            else: nums1ZeroCount += 1
        for num2 in nums2:
            if num2 > 0: nums2Pos.append(num2)
            elif num2 < 0: nums2Neg.append(- num2)
            else: nums2ZeroCount += 1
        nums1Neg.reverse()
        nums2Neg.reverse()
        neg = len(nums1Neg) * len(nums2Pos) + len(nums1Pos) * len(nums2Neg)
        if k <= neg: return - self.countKthSmallestProductOfFourSortedPositiveArrays(nums1Neg, nums2Pos, nums1Pos, nums2Neg, neg - k + 1)
        else: k -= neg
        zeros = (len(nums1Neg) + len(nums1Pos)) * nums2ZeroCount + (len(nums2Neg) + len(nums2Pos)) * nums1ZeroCount + nums1ZeroCount * nums2ZeroCount
        if k <= zeros: return 0
        else: k -= zeros
        return self.countKthSmallestProductOfFourSortedPositiveArrays(nums1Pos, nums2Pos, nums1Neg, nums2Neg, k)
# @lc code=end

