/*
 * @lc app=leetcode id=1095 lang=cpp
 *
 * [1095] Find in Mountain Array
 */

// @lc code=start
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

/**
 * This is MountainArray's API interface.
 * You should not implement it, or speculate about its implementation
 */

class Solution {
public:
    /*
    Firstly figure out the length of the whole array (1 call)
    Then figure out where is the peak by checking the local neighborhood (3logN calls)
    Reuse code from Leetcode 852. Peak Index in a Mountain Array
    Then binary search for the target on both sides of the peak
    return the lesser one if there are two
    */
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int left = 0, right = n, mid = -1;

        while (left < right) {
            mid = left + (right - left) / 2;
            vector<int> A = {mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)};
            if (A[0] < A[1] && A[1] > A[2]) {
                break;
            } else if (A[0] < A[1] && A[1] < A[2]) {
                left = mid;
            } else {
                right = mid;
            }
        }

        left = 0;
        right = mid + 1;

        while (left < right) {
            mid = left + (right - left) / 2;
            int num = mountainArr.get(mid);
            if (num == target) {
                return mid;
            } else if (num < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (left >= 0 && mountainArr.get(left) == target) {
            return left;
        }

        left = mid;
        right = n;

        while (left < right) {
            mid = left + (right - left) / 2;
            int num = mountainArr.get(mid);
            if (num == target) {
                return mid;
            } else if (num > target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (left < n && mountainArr.get(left) == target) {
            return left;
        }

        return -1;
    }
};

// @lc code=end

