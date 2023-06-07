/*
 * @lc app=leetcode id=1745 lang=cpp
 *
 * [1745] Palindrome Partitioning IV
 */

// @lc code=start
#include <string>;
#include <vector>;
using std::string;
using std::vector;
class Solution 
{
public:
    bool checkPartitioning(string s) 
    {
        int n = s.size();
        vector<vector<bool>> isPalindrome = {};
        vector<bool> row;
        for (int i = 0; i < n; i++)
        {
            row = {};
            for (int j = 0; j < n; j++)
            {
                row.push_back(false);
            }
            isPalindrome.push_back(row);
        }

        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                if (i == j) {
                    isPalindrome[i][j] = true;
                }
                else if ((isPalindrome[i + 1][j - 1] || j == i + 1) && s[i] == s[j]) {
                    isPalindrome[i][j] = true;
                }
            }
        }        

        for (int l = 1; l < n - 1; l++) {
            for (int r = l + 1; r < n; r++) {
                if (isPalindrome[0][l - 1] && isPalindrome[l][r - 1] && isPalindrome[r][n - 1]) {
                    return true;
                }
            }
        }

        return false;
    }
};
// @lc code=end

