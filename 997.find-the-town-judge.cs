/*
 * @lc app=leetcode id=997 lang=csharp
 *
 * [997] Find the Town Judge
 */

// @lc code=start
public class Solution 
{
    public int FindJudge(int n, int[][] trust) 
    {
        if (trust.Length == 0)
        {
            if (n == 1)
            {
                return n;
            }
        }
        else
        {
            HashSet<int> source = new HashSet<int>();
            Dictionary<int, int> sink = new Dictionary<int, int>();
            foreach (int[] pair in trust)
            {
                source.Add(pair[0]);
                if (!sink.ContainsKey(pair[1]))
                {
                    sink.Add(pair[1], 0);
                }
                sink[pair[1]]++;
            }
            for (int i = 1; i < n + 1; i++)
            {
                if (!source.Contains(i) && sink.ContainsKey(i) && sink[i] == n - 1)
                {
                    return i;
                }
            }
        }
        return -1;  
    }
}
// @lc code=end

