/*
 * @lc app=leetcode id=1658 lang=cpp
 *
 * [1658] Minimum Operations to Reduce X to Zero
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int x) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }

        int n = nums.size();
        if (total < x) {
            return -1;
        } else if (total == x) {
            return n;
        } else {
            int result = 0;
            int S = 0;
            int l = 0;

            for (int r = 0; r < n; r++) {
                S += nums[r];

                while (l < r && S > total - x) {
                    S -= nums[l];
                    l++;
                }

                if (S == total - x) {
                    result = std::max(result, r - l + 1);
                }
            }

            return result == 0 ? -1 : n - result;
        }
    }
};

// @lc code=end

