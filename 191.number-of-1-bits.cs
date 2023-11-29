/*
 * @lc app=leetcode id=191 lang=csharp
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
public class Solution {
    public int HammingWeight(uint n) {
        return Convert.ToString(n, 2).Count(c => c == '1');
    }
}

// @lc code=end

