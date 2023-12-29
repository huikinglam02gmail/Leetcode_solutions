/*
 * @lc app=leetcode id=2040 lang=cpp
 *
 * [2040] Kth Smallest Product of Two Sorted Arrays
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    long long kthSmallestProduct(std::vector<int>& nums1, std::vector<int>& nums2, long long k) {
        std::vector<int> nums1Pos, nums1Neg;
        long long nums1ZeroCount = 0;

        std::vector<int> nums2Pos, nums2Neg;
        long long nums2ZeroCount = 0;

        for (int num1 : nums1) {
            if (num1 > 0) {
                nums1Pos.push_back(num1);
            } else if (num1 < 0) {
                nums1Neg.push_back(-num1);
            } else {
                nums1ZeroCount++;
            }
        }

        for (int num2 : nums2) {
            if (num2 > 0) {
                nums2Pos.push_back(num2);
            } else if (num2 < 0) {
                nums2Neg.push_back(-num2);
            } else {
                nums2ZeroCount++;
            }
        }

        std::reverse(nums1Neg.begin(), nums1Neg.end());
        std::reverse(nums2Neg.begin(), nums2Neg.end());

        long long neg = static_cast<long long>(nums1Neg.size()) * static_cast<long long>(nums2Pos.size()) +
                        static_cast<long long>(nums1Pos.size()) * static_cast<long long>(nums2Neg.size());

        if (k <= neg) {
            return -countKthSmallestProductOfFourSortedPositiveArrays(nums1Neg, nums2Pos, nums1Pos, nums2Neg, neg - k + 1);
        } else {
            k -= neg;
        }

        long long zeros = (static_cast<long long>(nums1Neg.size()) + static_cast<long long>(nums1Pos.size())) * nums2ZeroCount +
                          (static_cast<long long>(nums2Neg.size()) + static_cast<long long>(nums2Pos.size())) * nums1ZeroCount +
                          nums1ZeroCount * nums2ZeroCount;

        if (k <= zeros) {
            return 0;
        } else {
            k -= zeros;
        }

        return countKthSmallestProductOfFourSortedPositiveArrays(nums1Pos, nums2Pos, nums1Neg, nums2Neg, k);
    }

private:
    long long countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(const std::vector<int>& arr1, const std::vector<int>& arr2, long long thres) {
        long long count = 0;
        int j = arr2.size() - 1;

        for (int num : arr1) {
            while (j >= 0 && static_cast<long long>(num) * static_cast<long long>(arr2[j]) > thres) {
                j--;
            }
            count += j + 1;
        }
        return count;
    }

    long long countKthSmallestProductOfFourSortedPositiveArrays(const std::vector<int>& arr1, const std::vector<int>& arr2, const std::vector<int>& arr3, const std::vector<int>& arr4, long long k) {
        long long l = LLONG_MAX;
        long long r = LLONG_MIN;

        if (!arr1.empty() && !arr2.empty()) {
            l = std::min(l, static_cast<long long>(arr1[0]) * static_cast<long long>(arr2[0]));
            r = std::max(r, static_cast<long long>(arr1.back()) * static_cast<long long>(arr2.back()) + 1);
        }

        if (!arr3.empty() && !arr4.empty()) {
            l = std::min(l, static_cast<long long>(arr3[0]) * static_cast<long long>(arr4[0]));
            r = std::max(r, static_cast<long long>(arr3.back()) * static_cast<long long>(arr4.back()) + 1);
        }

        while (l < r) {
            long long mid = l + (r - l) / 2;

            if (countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr1, arr2, mid) +
                countNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr3, arr4, mid) < k) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return l;
    }
};

// @lc code=end

