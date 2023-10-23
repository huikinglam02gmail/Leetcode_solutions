/*
 * @lc app=leetcode id=1955 lang=cpp
 *
 * [1955] Count Number of Special Subsequences
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int countSpecialSubsequences(std::vector<int>& nums) {
        std::vector<long> prev(3, 0);
        long MOD = 1000000007;

        for (int num : nums) {
            std::vector<long> next(3, 0);

            for (int i = 0; i < 3; i++) {
                next[i] += prev[i];

                if (i == num) {
                    next[i] += prev[i];
                    if (i > 0) {
                        next[i] += prev[i - 1];
                    }
                }

                next[i] %= MOD;
            }

            if (num == 0) {
                next[num] += 1;
            }

            prev = next;
        }

        return static_cast<int>(prev[2]);
    }
};

// @lc code=end

