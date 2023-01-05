/*
 * @lc app=leetcode id=2244 lang=csharp
 *
 * [2244] Minimum Rounds to Complete All Tasks
 */

// @lc code=start
public class Solution 
{
    public int MinimumRounds(int[] tasks) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        int maxValue = 0;
        int result = 0;
        foreach (int task in tasks)
        {
            if (!hashTable.ContainsKey(task))
            {
                hashTable.Add(task, 0);
            }
            hashTable[task]++;
            maxValue = Math.Max(hashTable[task], maxValue);
        }

        int[] dp = new int[maxValue + 1];
        dp[0] = 0;
        dp[1] = Int32.maxValue;
        for (int i = 2; i < maxValue + 1, i++)
        {
            dp[i] = 1;
            if (i > 3)
            {
                dp[i] += Math.Min(dp[i - 2], dp[i - 3]);
            }
        }
        foreach (int v in hashTable.Values)
        {
            result += dp[v];
        }
        if (result == Int32.maxValue)
        {
            return -1;
        }
        else
        {
            return result;
        }
    }
}
// @lc code=end

