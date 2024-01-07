/*
 * @lc app=leetcode id=2220 lang=csharp
 *
 * [2220] Minimum Bit Flips to Convert Number
 */

// @lc code=start
public class Solution {
    public int MinBitFlips(int start, int goal) {
        string binStart = Convert.ToString(start, 2).PadLeft(30, '0');
        string binGoal = Convert.ToString(goal, 2).PadLeft(30, '0');
        int result = 0;

        for (int i = 0; i < 30; i++) {
            if (binStart[i] != binGoal[i]) {
                result++;
            }
        }

        return result;
    }
}

// @lc code=end

