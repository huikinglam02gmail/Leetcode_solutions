/*
 * @lc app=leetcode id=228 lang=csharp
 *
 * [228] Summary Ranges
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        List<string> result = new List<string>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1] + 1))
            {
                result.Add(nums[i].ToString());
            }
            else if (i > 0 && nums[i] == nums[i - 1] + 1)
            {
                int ind = result.Last().IndexOf("->");
                result[result.Count - 1] = (ind >= 0 ? result.Last().Substring(0, ind) : result.Last()) + "->" + nums[i].ToString();
            }
        }
        return result;
    }
}
// @lc code=end

