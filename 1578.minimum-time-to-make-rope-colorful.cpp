/*
 * @lc app=leetcode id=1578 lang=cpp
 *
 * [1578] Minimum Time to Make Rope Colorful
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minCost(std::string colors, std::vector<int>& neededTime) {
        int i = 0, j = 0, result = 0, n = colors.length();
        
        while (i < n && j < n) {
            int S = 0, m = 0;
            while (j < n && colors[j] == colors[i]) {
                S += neededTime[j];
                m = std::max(m, neededTime[j]);
                j++;
            }
            result += S - m;
            i = j;
        }

        return result;
    }
};

// @lc code=end

