/*
 * @lc app=leetcode id=1798 lang=csharp
 *
 * [1798] Maximum Number of Consecutive Values You Can Make
 */

// @lc code=start
public class Solution {
    public int GetMaximumConsecutive(int[] coins) {
        Array.Sort(coins);
        int possible = 0;
        foreach (int coin in coins) 
        {
            if (possible + 1 < coin)
            {
                break;
            }
            else
            {
                possible += coin;
            }
        }
        return possible + 1;
    }
}
// @lc code=end

