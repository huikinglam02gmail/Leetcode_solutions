/*
 * @lc app=leetcode id=1833 lang=csharp
 *
 * [1833] Maximum Ice Cream Bars
 */

// @lc code=start
public class Solution 
{
    public int MaxIceCream(int[] costs, int coins) 
    {
        int n = costs.Length;
        Array.Sort(costs);
        for (int i = 0; i < n; i++)
        {
            if (coins < costs[i])
            {
                return i;
            }
            else
            {
                coins -= costs[i];
            }
        }    
        return n;
    }
}
// @lc code=end

