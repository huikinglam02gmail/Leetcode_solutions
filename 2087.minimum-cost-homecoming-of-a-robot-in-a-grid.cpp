/*
 * @lc app=leetcode id=2087 lang=cpp
 *
 * [2087] Minimum Cost Homecoming of a Robot in a Grid
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    /*
    There's no point going up one row and later go back down.
    */
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        int result = 0;
        int sign = startPos[0] <= homePos[0] ? 1 : -1;
        for (int i = startPos[0] + sign; i != homePos[0] + sign; i += sign) {
            result += rowCosts[i];
        }
        sign = startPos[1] <= homePos[1] ? 1 : -1;
        for (int i = startPos[1] + sign; i != homePos[1] + sign; i += sign) {
            result += colCosts[i];
        }
        return result;
    }
};

// @lc code=end

