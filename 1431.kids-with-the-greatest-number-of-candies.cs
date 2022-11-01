/*
 * @lc app=leetcode id=1431 lang=csharp
 *
 * [1431] Kids With the Greatest Number of Candies
 */

// @lc code=start
public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        int originalMax = candies.Max();
        List<bool> result = new List<bool>();
        foreach (int candy in candies)
        {
            result.Add(extraCandies + candy >= originalMax);
        }
        return result;
    }
}
// @lc code=end

