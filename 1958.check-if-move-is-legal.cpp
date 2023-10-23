/*
 * @lc app=leetcode id=1958 lang=cpp
 *
 * [1958] Check if Move is Legal
 */

// @lc code=start
class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
        int m = board.size();
        int n = board[0].size();
        
        vector<vector<int>> steps = {{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};
        
        unordered_map<char, char> opp = {{'B', 'W'}, {'W', 'B'}};
        
        for (int i = 0; i < 8; i++) {
            int x = rMove;
            int y = cMove;
            int countDiff = 0;
            
            while (x + steps[i][0] >= 0 && x + steps[i][0] < m && y + steps[i][1] >= 0 && y + steps[i][1] < n) {
                x += steps[i][0];
                y += steps[i][1];
                
                if (board[x][y] == opp[color]) {
                    countDiff++;
                }
                else if (board[x][y] == color && countDiff > 0) {
                    return true;
                }
                else {
                    break;
                }
            }
        }
        
        return false;
    }
};

// @lc code=end

