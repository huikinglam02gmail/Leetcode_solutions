/*
 * @lc app=leetcode id=905 lang=csharp
 *
 * [905] Sort Array By Parity
 */

// @lc code=start
public class Solution {
    public int[] SortArrayByParity(int[] nums) {
        return nums.OrderBy(x => x % 2).ToArray();
    }
}
// @lc code=end

