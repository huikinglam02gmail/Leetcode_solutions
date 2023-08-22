/*
 * @lc app=leetcode id=171 lang=cpp
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int n = columnTitle.length();
        int value = 0;
        int factor = 1;
        
        for (int i = n - 1; i >= 0; i--) {
            char c = columnTitle[i];
            value += (c - 'A' + 1) * factor;
            if (i > 0)
            {
                factor *= 26;
            }
        }
        
        return value;
    }
};

// @lc code=end

