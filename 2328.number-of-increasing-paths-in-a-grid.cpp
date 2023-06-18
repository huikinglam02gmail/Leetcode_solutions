/*
 * @lc app=leetcode id=2328 lang=cpp
 *
 * [2328] Number of Increasing Paths in a Grid
 */

// @lc code=start
#include <vector>
#include <map>
#include <tuple>

using std::make_tuple;
using std::tuple;
using std::map;
using std::vector;

class Solution 
{
private:
    vector<vector<int>> Grid;
    const long long MOD = 1000000007;
    map<tuple<int, int>, int> memo;
    int DFS(int row, int col) 
    {
        tuple<int, int> t = make_tuple(row, col);
        if (memo.find(t) == memo.end()) 
        {
            long long result = 1;

            if (row + 1 < Grid.size() && Grid[row + 1][col] > Grid[row][col]) 
            {
                result += DFS(row + 1, col);
                result %= MOD;
            }

            if (col + 1 < Grid[0].size() && Grid[row][col + 1] > Grid[row][col]) 
            {
                result += DFS(row, col + 1);
                result %= MOD;
            }

            if (row > 0 && Grid[row - 1][col] > Grid[row][col]) 
            {
                result += DFS(row - 1, col);
                result %= MOD;
            }

            if (col > 0 && Grid[row][col - 1] > Grid[row][col]) 
            {
                result += DFS(row, col - 1);
                result %= MOD;
            }

            memo[t] = (int)(result);
        }
        return memo[t];
    }
public:
    int countPaths(vector<vector<int>>& grid) 
    {
        Grid = grid;
        long long result = 0;
        int m = grid.size();
        int n = grid[0].size();

        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                result += DFS(i, j);
                result %= MOD;
            }
        }

        return (int)(result);
    }
};

// @lc code=end

