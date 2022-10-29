/*
 * @lc app=leetcode id=2136 lang=csharp
 *
 * [2136] Earliest Possible Day of Full Bloom
 */

// @lc code=start
public class Solution {
    public int EarliestFullBloom(int[] plantTime, int[] growTime) {
        Array.Sort(growTime, plantTime);
        int n = growTime.Length;
        int result = 0;
        int plantCumu = 0;
        for (int i=n-1;i>=0;i--)
        {
            result = Math.Max(result, plantCumu + plantTime[i] + growTime[i]);
            plantCumu += plantTime[i];
        }
        return result;
    }
}
// @lc code=end

