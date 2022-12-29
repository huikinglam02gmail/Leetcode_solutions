/*
 * @lc app=leetcode id=1575 lang=csharp
 *
 * [1575] Count All Possible Routes
 */

// @lc code=start
public class Solution 
{
    Dictionary<Tuple<int, int>, long> memo = new Dictionary<Tuple<int, int>, long>();
    long MOD = 1000000007;
    int fin;
    int n;
    int[] Locations;
    public long dfs(int loc, int f)
    {
        Tuple<int, int> t = new Tuple<int, int>(loc, f);
        long result = 0;
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else if (f >= 0)
        {
            if (loc == fin)
            {
                result++;
            }
            for (int i = 0; i < n; i++)
            {
                if (i !=  loc)
                {
                    result += dfs(i, f - Math.Abs(Locations[i] - Locations[loc]));
                    result %= MOD;
                }
            }
        }
        memo.Add(t, result);
        return result;
    }
    public int CountRoutes(int[] locations, int start, int finish, int fuel) 
    {
        fin = finish;
        n = locations.Length;
        Locations = locations;
        return Convert.ToInt32(dfs(start, fuel));
    }
}
// @lc code=end

