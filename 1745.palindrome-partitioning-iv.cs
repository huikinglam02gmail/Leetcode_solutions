/*
 * @lc app=leetcode id=1745 lang=csharp
 *
 * [1745] Palindrome Partitioning IV
 */

// @lc code=start
public class Solution {
    public bool CheckPartitioning(string s) {
        int n = s.Length;
        bool[][] isPalindrome = new bool[n][];
        for (int i = 0; i < n; i++) {
            isPalindrome[i] = new bool[n];
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
}

// @lc code=end

