/*
 * @lc app=leetcode id=1553 lang=csharp
 *
 * [1553] Minimum Number of Days to Eat N Oranges
 */

// @lc code=start
public class Solution 
{
    Dictionary<int, int> memo = new Dictionary<int, int>();
    public int dp(int i)
    {
        if (memo.ContainsKey(i))
        {
            return memo[i];
        }
        else if (i < 2)
        {
            return i;
        }
        else
        {
            int result = 1 + Math.Min(i % 3 + dp(i / 3), i % 2 + dp(i / 2));
            memo.Add(i, result);
            return result;
        }
    }
    public int MinDays(int n) 
    {
        return dp(n);
    }
}
// @lc code=end

