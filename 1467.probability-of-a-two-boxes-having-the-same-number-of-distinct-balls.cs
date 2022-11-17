/*
 * @lc app=leetcode id=1467 lang=csharp
 *
 * [1467] Probability of a Two Boxes Having The Same Number of Distinct Balls
 */

// @lc code=start
public class Solution 
{
    int total;
    int[] Balls;

    // Returns value of Binomial
    // Coefficient C(n, k)
    public long comb(int n, int k)
    {
        long res = 1;
 
        // Since C(n, k) = C(n, n-k)
        if (k > n - k)
            k = n - k;
 
        // Calculate value of [n * ( n - 1) *---* (
        // n - k + 1)] / [k * (k - 1) *----* 1]
        for (int i = 0; i < k; i++) {
            res *= (n - i);
            res /= (i + 1);
        }
 
        return res;
    }

    public long dp(int i, int num1, int color1, int num2, int color2)
    {
        if (num1 > total / 2)
        {
            return 0;
        }
        if (num1 > total / 2)
        {
            return 0;
        }
        if (i == Balls.Length)
        {
            if (num1 == total / 2 && num2 == total /  2 && color1 == color2)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        long result = 0;
        for (int j = 0; j < Balls[i]+1; j++)
        {
            long multiplicity = comb(Balls[i], j);
            int color1New = color1;
            int color2New = color2;
            if (j > 0)
            {
                color1New += 1;
            }
            if (j < Balls[i])
            {
                color2New += 1;
            }
            result += multiplicity*dp(i+1, num1+j, color1New, num2+Balls[i]-j, color2New);
        }
        return result;
    }

    public double GetProbability(int[] balls) 
    {
        Balls = balls;
        total = Balls.Sum();
        return (double) dp(0,0,0,0,0) / (double) comb(total, total / 2);
    }
}
// @lc code=end

