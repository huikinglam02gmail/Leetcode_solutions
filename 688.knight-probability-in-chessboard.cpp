/*
 * @lc app=leetcode id=688 lang=cpp
 *
 * [688] Knight Probability in Chessboard
 */

// @lc code=start
#include<vector>
#include<utility>
using std::pair;
using std::vector;
class Solution {
private:
    bool insideBoard(int row, int col, int n) {
        return row >= 0 && row < n && col >= 0 && col < n;
    }
    
public:
    double knightProbability(int n, int k, int row, int column) {
        vector<vector<int>> possibleSteps = {
            {1, 2},
            {2, 1},
            {2, -1},
            {1, -2},
            {-1, -2},
            {-2, -1},
            {-2, 1},
            {-1, 2}
        };
        
        vector<vector<vector<pair<int, int>>>> destination(n, vector<vector<pair<int, int>>>(n, vector<pair<int, int>>{}));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (const auto& possibleStep : possibleSteps) {
                    int newRow = i + possibleStep[0];
                    int newCol = j + possibleStep[1];
                    if (insideBoard(newRow, newCol, n))
                        destination[i][j].push_back({ newRow, newCol });
                }
            }
        }
        
        vector<vector<double>> dpOld(n, vector<double>(n));
        dpOld[row][column] = 1.0;
        
        for (int run = 0; run < k; run++) {
            vector<vector<double>> dpNew(n, vector<double>(n));
            
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dpOld[i][j] > 0.0) {
                        for (const pair<int, int>& item : destination[i][j]) {
                            dpNew[item.first][item.second] += dpOld[i][j];
                        }
                    }
                }
            }
            
            dpOld = dpNew;
        }
        
        double result = 0.0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result += dpOld[i][j];
            }
        }
        
        return result / pow(8, k);
    }
};

// @lc code=end

