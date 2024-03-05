/*
 * @lc app=leetcode id=3028 lang=cpp
 *
 * [3028] Ant on the Boundary
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int result = 0;
        int x = 0;
        for (int num : nums) {
            x += num;
            if (x == 0) result++;
        }
        return result;
    }
};

// @lc code=end

