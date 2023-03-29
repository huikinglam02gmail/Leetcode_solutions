/*
 * @lc app=leetcode id=1402 lang=csharp
 *
 * [1402] Reducing Dishes
 */

// @lc code=start
using System.Linq;
public class Solution 
{
    public int MaxSatisfaction(int[] satisfaction) 
    {
        satisfaction = satisfaction.OrderBy(x => x).ToArray();
        int result = 0;
        int current = 0;
        int i = satisfaction.Length - 1;
        while (i >= 0 && satisfaction[i] + current > 0)
        {
            current += satisfaction[i];
            i--;
            result += current;
        }  
        return result;
    }
}
// @lc code=end

