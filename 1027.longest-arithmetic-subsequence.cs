/*
 * @lc app=leetcode id=1027 lang=csharp
 *
 * [1027] Longest Arithmetic Subsequence
 */

// @lc code=start
public class Solution {
    public int LongestArithSeqLength(int[] nums) {
        int n = nums.Length;
        Dictionary<(int, int), int> dp = new Dictionary<(int, int), int>();
        
        for (int i = 1; i < n; i++)
        {
            for (int k = 0; k < i; k++)
            {
                int difference = nums[i] - nums[k];
                if (dp.ContainsKey((k, difference)))
                {
                    dp[(i, difference)] = 1 + dp[(k, difference)];
                }
                else
                {
                    dp[(i, difference)] = 2;
                }
            }
        }
        
        int maxLength = 0;
        foreach (int length in dp.Values)
        {
            maxLength = Math.Max(maxLength, length);
        }
        
        return maxLength;
    }
}
// @lc code=end

