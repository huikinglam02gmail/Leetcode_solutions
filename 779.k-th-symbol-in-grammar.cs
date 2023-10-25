/*
 * @lc app=leetcode id=779 lang=csharp
 *
 * [779] K-th Symbol in Grammar
 */

// @lc code=start
public class Solution {
    public int KthGrammar(int n, int k) {
        return Convert.ToInt32((n > 1 || k > 1) && ((1 - (k % 2) ^ KthGrammar(n - 1, (k + 1) / 2)) == 1));      
    }
}
// @lc code=end

