/*
 * @lc app=leetcode id=1449 lang=csharp
 *
 * [1449] Form Largest Integer With Digits That Add up to Target
 */

// @lc code=start
public class Solution 
{
    public string largerOfTwoIntegerStrings(string s1, string s2)
    {
        if (s1.Length > s2.Length)
        {
            return s1;
        }
        else if (s1.Length < s2.Length)
        {
            return s2;
        }
        else if (string.Compare(s1, s2) < 0)
        {
            return s2;
        }
        else
        {
            return s1;
        }
    }
    public string LargestNumber(int[] cost, int target) 
    {
        Dictionary<int, int> Costs = new Dictionary<int, int>();
        string[] dp = new string[target + 1];

        for (int i = 0; i < cost.Length; i++)
        {
            Costs[cost[i]] = i + 1;
        }

        Array.Fill(dp, "0");
        for (int t = 1; t < target + 1; t++)
        {
            foreach (KeyValuePair<int, int> kvp in Costs)
            {
                string candidate = "0";
                if (t == kvp.Key)
                {
                    candidate = kvp.Value.ToString();
                }
                else if (t > kvp.Key && !dp[t - kvp.Key].Equals("0"))
                {
                    char[] newCandidate = new char[dp[t - kvp.Key].Length + 1];
                    for (int i = 0; i < dp[t - kvp.Key].Length; i++)
                    {
                        newCandidate[i] = dp[t - kvp.Key][i];
                    }
                    newCandidate[dp[t - kvp.Key].Length] = (char) (kvp.Value + '0');
                    Array.Sort(newCandidate);
                    Array.Reverse(newCandidate);
                    candidate = string.Join("", newCandidate);
                }
                dp[t] = largerOfTwoIntegerStrings(dp[t], candidate);
            }
        }
        return dp[target];
    }
}
// @lc code=end

