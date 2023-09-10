/*
 * @lc app=leetcode id=1359 lang=csharp
 *
 * [1359] Count All Valid Pickup and Delivery Options
 */

// @lc code=start
public class Solution {
    public int CountOrders(int n) {
        long result = 1;
        long MOD = 1000000007;

        for (int i = 2; i <= n; i++) {
            result *= i;
            result %= MOD;
            result *= 2 * i - 1;
            result %= MOD;
        }

        return (int)result;
    }
}

// @lc code=end

