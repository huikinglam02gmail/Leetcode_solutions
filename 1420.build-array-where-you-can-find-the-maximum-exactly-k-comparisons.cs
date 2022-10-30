/*
 * @lc app=leetcode id=1420 lang=csharp
 *
 * [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
 */

// @lc code=start
public class Solution {
    const long MOD = 1000000007;
    Dictionary<Tuple<int,int,int>,long> memo = new Dictionary<Tuple<int,int,int>,long>();
    public long dp(int i, int j, int l)
    {
        Tuple<int, int, int> key = new Tuple<int, int, int>(i, j, l);
        if (memo.ContainsKey(key))
        {
            return memo[key];
        }
        else
        {
            long result = 0;
            if (i == 1 && l == 1)
            {
                result += 1;
            }
            else if (i > 1)
            {
                result += j*dp(i-1,j,l);
                result %= MOD;
                if (l > 1)
                {
                    for (int x = 1; x < j; x++)
                    {
                        result += dp(i-1,x,l-1);
                        result %= MOD;
                    }
                }
            }
            memo.Add(key, result);
            return result;
        }

    }
    public int NumOfArrays(int n, int m, int k) 
    {
        long final = 0;
        for (int i = 1; i < m+1; i++)
        {
            final += dp(n, i, k);
            final %= MOD;
        }
        return (int) final;
    }
}
// @lc code=end

