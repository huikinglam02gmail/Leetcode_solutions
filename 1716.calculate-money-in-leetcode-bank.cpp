/*
 * @lc app=leetcode id=1716 lang=cpp
 *
 * [1716] Calculate Money in Leetcode Bank
 */

// @lc code=start
class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;
        int result = 0;

        for (int i = 0; i < weeks; i++) {
            result += 28 + i * 7;
        }

        for (int i = 0; i < days; i++) {
            result += (i + 1) + weeks;
        }

        return result;
    }
};

// @lc code=end

