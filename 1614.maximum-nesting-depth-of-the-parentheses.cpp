/*
 * @lc app=leetcode id=1614 lang=cpp
 *
 * [1614] Maximum Nesting Depth of the Parentheses
 */

// @lc code=start
#include <string>
#include <algorithm>

class Solution {
public:
    /*
    Keep track of which level you're at, and the historical max
    */
    int maxDepth(std::string s) {
        int currentMax = 0;
        int current = 0;
        for (char c : s) {
            if (c == '(') {
                current++;
                currentMax = std::max(currentMax, current);
            } else if (c == ')') {
                current--;
            }
        }
        return currentMax;
    }
};

// @lc code=end

