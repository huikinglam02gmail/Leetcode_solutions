/*
 * @lc app=leetcode id=1053 lang=cpp
 *
 * [1053] Previous Permutation With One Swap
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
     * To find previous permutation (with one swap), follow this algorithm:
     * Find largest index i such that arr[i] > arr[i+1], for 0 <= i < n-1
     * If the i found is -1: return arr
     * Find largest index j such that j > i and arr[j] < arr[i].
     * Swap arr[i] and arr[j]
     * Return arr
     */
    std::vector<int> prevPermOpt1(std::vector<int>& arr) {
        int n = arr.size();
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (j > i && arr[i] <= arr[j]) {
                j--;
            }
            while (j > 0 && arr[j - 1] == arr[j]) {
                j--;
            }
            std::swap(arr[i], arr[j]);
        }
        return arr;
    }
};

// @lc code=end

