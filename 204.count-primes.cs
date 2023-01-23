/*
 * @lc app=leetcode id=204 lang=csharp
 *
 * [204] Count Primes
 */

// @lc code=start
public class Solution 
{
    public int CountPrimes(int n) 
    {
        if (n < 2)
        {
            return 0;
        }    
        bool[] prime = new bool[n];
        Array.Fill(prime, true);
        int result = 0;
        long i = 2;
        while (i < n)
        {
            if (prime[i])
            {
                for (long j = i*i; j < n; j+=i)
                {
                    prime[j] = false;
                }
                result++;
            }
            i++;
        }
        return result;
    }
}
// @lc code=end
