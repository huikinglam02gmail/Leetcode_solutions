/*
 * @lc app=leetcode id=1351 lang=cpp
 *
 * [1351] Count Negative Numbers in a Sorted Matrix
 */

// @lc code=start
#include <vector>;
using std::vector;
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) 
    {
        int result = 0;
        int m = grid.size();
        int n = grid[0].size();
        int x = 0;
        int y = n - 1;
        
        while (x < m && y >= 0)
        {
            if (grid[x][y] >= 0)
            {
                result += n - 1 - y;
                x++;
            }
            else
            {
                y--;
            }
        }
        
        if (y < 0)
        {
            result += (m - x) * n;
        }
        
        return result;    
    }
};
// @lc code=end

