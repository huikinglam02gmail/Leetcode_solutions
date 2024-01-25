/*
 * @lc app=leetcode id=2582 lang=csharp
 *
 * [2582] Pass the Pillow
 */

// @lc code=start
public class Solution {
    /**
     * Simple math. One cycle takes 2 * (n - 1)
     * Take the modulo time % (2 * (n - 1)) = t. Then I will hold the ball at times i - 1 and 2 * (n - 1) - (i - 1) = 2 * n - i - 1
     * So if 1 <= t + 1 <= n, return t + 1
     * else return 2 * n - 1 - t
     */
    public int PassThePillow(int n, int time) {
        int t = time % (2 * (n - 1));
        if (0 <= t && t <= n - 1) {
            return t + 1;
        } else {
            return 2 * n - 1 - t;
        }
    }
}

// @lc code=end

