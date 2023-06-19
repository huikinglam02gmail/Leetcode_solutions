/*
 * @lc app=leetcode id=1732 lang=cpp
 *
 * [1732] Find the Highest Altitude
 */

// @lc code=start
#include<vector>;
#include <algorithm>;
using std::max;
using std::vector;
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int currentMax = 0;
        int currentHeight = 0;
        for (int i : gain) {
            currentHeight += i;
            currentMax = max(currentMax, currentHeight);
        }
        return currentMax;       
    }
};
// @lc code=end

