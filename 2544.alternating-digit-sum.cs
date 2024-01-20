/*
 * @lc app=leetcode id=2544 lang=csharp
 *
 * [2544] Alternating Digit Sum
 */

// @lc code=start
public class Solution {
    public int AlternateDigitSum(int n) {
        int result = 0;
        int sign = 1;

        foreach (char c in n.ToString()) {
            result += sign * int.Parse(c.ToString());
            sign *= -1;
        }

        return result;
    }
}

// @lc code=end

