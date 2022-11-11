/*
 * @lc app=leetcode id=1447 lang=csharp
 *
 * [1447] Simplified Fractions
 */

// @lc code=start
public class Solution 
{
    public int gcd(int a, int b)
    {
        if (a < b)
        {
            int temp =  a;
            a = b;
            b = temp;
        }
        if (b == 0)
        {
            return a;
        }
        else
        {
            return gcd(b, a % b);
        }
    }
    public IList<string> SimplifiedFractions(int n) 
    {
        if (n == 1)
        {
            return new List<string>();
        }
        else
        {
            HashSet<string> result = new HashSet<string>();
            for (int i = 2; i < n + 1; i++)
            {
                for (int j = 1; j < i; j++)
                {
                    result.Add((j / gcd(i,j)).ToString() + '/' + (i / gcd(i,j)).ToString());
                }
            }
            return result.ToList();
        }    
    }
}
// @lc code=end

