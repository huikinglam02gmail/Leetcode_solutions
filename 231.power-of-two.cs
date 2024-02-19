/*
 * @lc app=leetcode id=231 lang=csharp
 *
 * [231] Power of Two
 */

// @lc code=start
public class Solution {
    public bool IsPowerOfTwo(int n) {
        if (n == 2 || n == 1) {
            return true;
        } else if (n < 1 || n % 2 != 0) {
            return false;
        } else {
            return IsPowerOfTwo(n / 2);
        }
    }
}

// @lc code=end

