/*
 * @lc app=leetcode id=1434 lang=csharp
 *
 * [1434] Number of Ways to Wear Different Hats to Each Other
 */

// @lc code=start
public class Solution {
    public int NumberWays(IList<IList<int>> hats) {
        int n = hats.Count;
        long MOD = 1000000007;
        Dictionary<int, List<int>> hatToPeople = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++)
        {
            List<int> hatList = new List<int>(hats[i]);
            hatList.Sort();
            foreach (int hat in hatList)
            {
                if (!hatToPeople.ContainsKey(hat-1))
                {
                    hatToPeople.Add(hat-1, new List<int>());
                }
                hatToPeople[hat-1].Add(i);
            }
        }
        Dictionary <int, HashSet<Tuple<int, int>>> prePostSwitch = new Dictionary<int, HashSet<Tuple<int, int>>>();
        for (int i = 0; i < (1<<n); i++)
        {
            for (int j = 0; j < n; j++)
            {
                if ((i & (1<<j)) != 0)
                {
                    (int, int) t = (i^(1<<j),i);
                    if (!prePostSwitch.ContainsKey(j))
                    {
                        prePostSwitch[j] = new HashSet<Tuple<int, int>>();
                    }
                    prePostSwitch[j].Add(t.ToTuple());
                }
            }
        }
        long[] dp = new long[1 << n];
        Array.Clear(dp, 0, 1 << n);
        long[] dpNew = new long[1 << n];
        for (int h = 0; h < 40; h++)
        {
            Array.Copy(dp, dpNew, 1 << n);
            if (hatToPeople.ContainsKey(h))
            {
                foreach (int i in hatToPeople[h])
                {
                    foreach(Tuple<int,int> t in prePostSwitch[i])
                    {
                        int pre = t.Item1;
                        int post = t.Item2;
                        if (pre == 0)
                        {
                            dpNew[post] += 1;
                        }
                        else
                        {
                            dpNew[post] += dp[pre];
                        }
                        dpNew[post] %= MOD;
                    }
                }
            }
            Array.Copy(dpNew, dp, 1<<n);
        }
        return (int) dp[(1<<n)-1];
    }
}
// @lc code=end

