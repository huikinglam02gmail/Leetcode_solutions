/*
 * @lc app=leetcode id=1648 lang=csharp
 *
 * [1648] Sell Diminishing-Valued Colored Balls
 */

// @lc code=start
public class Solution 
{
    public int MaxProfit(int[] inventory, int orders) 
    {
        long MOD = 1000000007;
        long order = Convert.ToInt64(orders);
        List<int[]> counter = inventory.OrderBy(r => -r).GroupBy(p => p).Select(g => new int[2]{g.Key, g.Count()}).ToList();
        counter.Add(new int[2]{0,0});

        long result = 0;
        long width = 0;
        int ind = 0;

        while (order > 0)
        {
            width += Convert.ToInt64(counter[ind][1]);
            long sell = Math.Min(order, width * (counter[ind][0] - counter[ind + 1][0]));
            long q = Math.DivRem(sell, width, out long r);
            result += width * (2 * q * counter[ind][0] + q - q * q) / 2;
            result += (counter[ind][0] - q) * r;
            result %= MOD;
            if (result < 0)
            {
                result += MOD;
                result %= MOD;
            }
            order -= width * q;
            order -= r;
            ind += 1;            
        }

        return Convert.ToInt32(result);
    }
}
// @lc code=end
