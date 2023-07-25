/*
 * @lc app=leetcode id=852 lang=cpp
 *
 * [852] Peak Index in a Mountain Array
 */

// @lc code=start
#include<vector>
using std::vector;
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 0;
        int right = arr.size();

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1]) {
                left = mid;
            } else if (arr[mid - 1] > arr[mid] && arr[mid] > arr[mid + 1]) {
                right = mid;
            } else if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1]) {
                return mid;
            } else {
                return -1;
            }
        }

        return -1; // In case there's no peak found.
    }
};
// @lc code=end

