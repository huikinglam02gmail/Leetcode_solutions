/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
private:
    /*
    DFS
    Append "0" to the edge such that I can avoid edge effect codes
    Then DFS from every point
    */
    bool dfs(int row, int col, string word) {
        if (word.empty()) {
            return true;
        } else if (board[row][col] == word[0]) {
            board[row][col] = '0';
            vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (const auto& direction : directions) {
                if (dfs(row + direction[0], col + direction[1], word.substr(1))) return true;
            }
            board[row][col] = word[0];
        }
        return false;
    }
    
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        if (word.length() > m * n) return false;
        unordered_map<char, int> boardDict;
        unordered_map<char, int> wordDict;

        for (char c = 'a'; c <= 'z'; ++c) {
            boardDict[c] = 0;
            wordDict[c] = 0;
        }
        
        for (const auto& row : board) {
            for (char c : row) {
                boardDict[c]++;
            }
        }
        
        for (char c : word) {
            wordDict[c]++;
        }
        
        for (char c = 'a'; c <= 'z'; ++c) {
            if (wordDict[c] > boardDict[c]) return false;
        }
        
        if (wordDict[word[0]] > wordDict[word[word.length() - 1]]) {
            reverse(word.begin(), word.end());
        }

        this->board = vector<vector<char>>(m + 2, vector<char>(n + 2, '0'));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                this->board[i + 1][j + 1] = board[i][j];
            }
        }

        for (int i = 1; i < m + 1; ++i) {
            for (int j = 1; j < n + 1; ++j) {
                if (dfs(i, j, word)) return true;
            }
        }
        return false;
    }
    
private:
    vector<vector<char>> board;
};
// @lc code=end

