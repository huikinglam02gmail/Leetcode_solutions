/*
 * @lc app=leetcode id=1601 lang=csharp
 *
 * [1601] Maximum Number of Achievable Transfer Requests
 */

// @lc code=start
public class Solution 
{
    public int MaximumRequests(int n, int[][] requests) 
    {
        int result = 0;
        int m = requests.Length;
        for (int mask = 0; mask < (1 << m); mask++)
        {
            int[] flow = new int[n];
            Array.Fill(flow, 0);
            int count = 0;
            for (int j = 0; j < m; j++)
            {
                if ((mask & (1 << j)) != 0)
                {
                    flow[requests[j][0]]--;
                    flow[requests[j][1]]++;
                    count++;
                }
            }
            if (flow.All(x => x == 0))
            {
                result = Math.Max(result, count);
            }
        }
        return result;    
    }
}
// @lc code=end

