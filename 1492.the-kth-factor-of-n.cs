/*
 * @lc app=leetcode id=1492 lang=csharp
 *
 * [1492] The kth Factor of n
 */

// @lc code=start
public class Solution 
{
    public int KthFactor(int n, int k) 
    {
        int i = 1;
        SortedSet<int> factors = new SortedSet<int>();
        while (i*i <= n)
        {
            if (n % i == 0)
            {
                factors.Add(i);
                factors.Add(n / i);
            }
            i++;
        }
        if (k > factors.Count)
        {
            return -1;
        }
        else
        {
            return factors.ElementAt(k-1);
        }
    }
}
// @lc code=end

