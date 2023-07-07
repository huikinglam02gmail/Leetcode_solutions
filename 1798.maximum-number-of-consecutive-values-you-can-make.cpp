/*
 * @lc app=leetcode id=1798 lang=cpp
 *
 * [1798] Maximum Number of Consecutive Values You Can Make
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::sort;
using std::vector;
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int possible = 0;
        for (int coin : coins) 
        {
            if (possible + 1 < coin)
            {
                break;
            }
            else
            {
                possible += coin;
            }
        }
        return possible + 1;
    }
};
// @lc code=end

