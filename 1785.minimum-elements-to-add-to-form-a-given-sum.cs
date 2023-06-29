/*
 * @lc app=leetcode id=1785 lang=csharp
 *
 * [1785] Minimum Elements to Add to Form a Given Sum
 */

// @lc code=start
public class Solution {
    public int MinElements(int[] nums, int limit, int goal) {
        return Convert.ToInt32((Math.Abs(nums.Select(x => Convert.ToInt64(x)).Sum() - Convert.ToInt64(goal)) + Convert.ToInt64(limit) - 1) / Convert.ToInt64(limit));
    }
}
// @lc code=end

