/*
 * @lc app=leetcode id=2928 lang=cpp
 *
 * [2928] Distribute Candies Among Children I
 */

// @lc code=start
class Solution {
public:
    int distributeCandies(int n, int limit) {
        int result = 0;
        for (int i = 0; i <= limit; i++) {
            for (int j = 0; j <= limit; j++) {
                for (int k = 0; k <= limit; k++) {
                    if (i + j + k == n) {
                        result++;
                    }
                }
            }
        }
        return result;
    }
};

// @lc code=end

