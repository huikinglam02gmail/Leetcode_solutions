/*
 * @lc app=leetcode id=1850 lang=cpp
 *
 * [1850] Minimum Adjacent Swaps to Reach the Kth Smallest Number
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (j > i && nums[i] >= nums[j]) {
                j--;
            }
            std::swap(nums[i], nums[j]);
        }

        i++;
        int end = n - 1;
        while (i < end) {
            std::swap(nums[i], nums[end]);
            i++;
            end--;
        }
    }

    int getMinSwaps(std::string num, int k) {
        std::vector<int> target;
        for (char c : num) {
            target.push_back(c - '0');
        }
        for (int i = 0; i < k; i++) {
            nextPermutation(target);
        }
        std::vector<int> original;
        for (char c : num) {
            original.push_back(c - '0');
        }
        int result = 0;
        int n = original.size();
        for (int i = 0; i < n; i++) {
            int j = i;
            while (original[j] != target[i]) {
                j++;
            }
            while (j > i) {
                std::swap(original[j], original[j - 1]);
                j--;
                result++;
            }
        }
        return result;
    }
};
// @lc code=end

