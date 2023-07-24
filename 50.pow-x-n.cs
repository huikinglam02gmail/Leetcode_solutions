/*
 * @lc app=leetcode id=50 lang=csharp
 *
 * [50] Pow(x, n)
 */

// @lc code=start
public class Solution {
    public double MyPow(double x, int n) {
        long y = n >= 0 ? n : -(long)n; // Use long to prevent overflow when n is Int32.MinValue
        double result = 1.0;
        
        while (y > 0) {
            if (y % 2 == 0) {
                x *= x;
                y /= 2;
            } else {
                result *= x;
                y -= 1;
            }
        }
        
        return n >= 0 ? result : 1.0 / result;
    }
}

// @lc code=end

