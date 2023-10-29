/*
 * @lc app=leetcode id=1969 lang=csharp
 *
 * [1969] Minimum Non-Zero Product of the Array Elements
 */

// @lc code=start
public class Solution {
    public int ModPow(long x, long y, int m) {
        if (y == 0)
            return 1;
        long p = ModPow(x, y / 2, m);
        p = (p * p) % m;
        return y % 2 == 1 ? (int)((p * (x % m)) % m) : (int)p;
    }

    public int MinNonZeroProduct(int p) {
        long cnt = (1L << p) - 1;
        int mod = 1000000007;
        return (int)((cnt % mod) * ModPow(cnt - 1, cnt / 2, mod) % mod);
    }
}


// @lc code=end

