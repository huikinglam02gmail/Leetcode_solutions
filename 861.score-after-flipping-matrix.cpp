/*
 * @lc app=leetcode id=861 lang=cpp
 *
 * [861] Score After Flipping Matrix
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /*
    Greedy approach
    First column is larger than sum of all on the right
    1000 = 8 > 0111 = 7
    Therefore, one must flip all rows with first column 0s to 1s
    Then for each column, count max(# 1s, # 0s)    
    */
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < n; j++) {
                    grid[i][j] = (grid[i][j] == 0) ? 1 : 0;
                }
            }
        }
        int score = 0;
        for (int j = 0; j < n; j++) {
            vector<int> col;
            for (int i = 0; i < m; i++) {
                col.push_back(grid[i][j]);
            }
            score += (1 << (n - 1 - j)) * max(count(col.begin(), col.end(), 1), count(col.begin(), col.end(), 0));
        }
        return score;
    }
};

// @lc code=end

