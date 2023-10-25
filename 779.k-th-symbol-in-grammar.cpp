/*
 * @lc app=leetcode id=779 lang=cpp
 *
 * [779] K-th Symbol in Grammar
 */

// @lc code=start
class Solution {
public:
    int kthGrammar(int n, int k) {
        return (int)((n > 1 || k > 1) && ((1 - (k % 2) ^ kthGrammar(n - 1, (k + 1) / 2)) == 1));
    }
};
// @lc code=end

