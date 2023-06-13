/*
 * @lc app=leetcode id=2352 lang=cpp
 *
 * [2352] Equal Row and Column Pairs
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::equal;
using std::vector;
class Solution 
{
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix)
    {
        vector<vector<int>> transposed{};
        for (int i = 0; i < matrix[0].size(); i++)
        {
            vector<int> row;
            for (int j = 0; j < matrix.size(); j++)
            {
                row.push_back(matrix[j][i]);
            }
            transposed.push_back(row);
        }
        return transposed;
    }

    int equalPairs(vector<vector<int>>& grid) 
    {
        auto transposedGrid = transpose(grid);
        int result = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid.size(); j++)
            {
                if (equal(grid[i].begin(), grid[i].begin() + grid.size(), transposedGrid[j].begin()))
                {
                    result++;
                }
            }
        }
        return result;
    }
};
// @lc code=end

