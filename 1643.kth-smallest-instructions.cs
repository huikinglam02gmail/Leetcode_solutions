/*
 * @lc app=leetcode id=1643 lang=csharp
 *
 * [1643] Kth Smallest Instructions
 */

// @lc code=start
public class Solution 
{
    static long ncr(int n, int r)
    {
 
        // p holds the value of n*(n-1)*(n-2)...,
        // k holds the value of r*(r-1)...
        long p = 1, k = 1;
 
        // C(n, r) == C(n, n-r),
        // choosing the smaller value
        if (n - r < r) 
        {
            r = n - r;
        }
 
        if (r != 0) 
        {
            while (r > 0) 
            {
                p *= n;
                k *= r;
 
                // gcd of p, k
                long m = __gcd(p, k);
 
                // dividing by gcd, to simplify
                // product division by their gcd
                // saves from the overflow
                p /= m;
                k /= m;
 
                n--;
                r--;
            }
 
            // k should be simplified to 1
            // as C(n, r) is a natural number
            // (denominator should be 1 ) .
        }
        else 
        {
            p = 1;
        }

        // if our approach is correct p = ans and k =1
        return p;
    }
 
    static long __gcd(long n1, long n2)
    {
        long gcd = 1;
 
        for (int i = 1; i <= n1 && i <= n2; ++i) {
            // Checks if i is factor of both integers
            if (n1 % i == 0 && n2 % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }
    
    public string KthSmallestPath(int[] destination, int k) 
    {
        if (destination[0] == 0)
        {
            return new string('H', destination[1]);
        }
        else if (destination[1] == 0)
        {
            return new string('V', destination[0]);
        }
        else
        {
            long total = ncr(destination.Sum(), destination[0]);
            if (k <= total * destination[1] / destination.Sum())
            {
                return "H" + KthSmallestPath(new int[2]{destination[0], destination[1] - 1}, k);
            }
            else
            {
                return "V" + KthSmallestPath(new int[2]{destination[0] - 1, destination[1]}, Convert.ToInt32(k - total * destination[1] / destination.Sum()));
            }
        }
    }
}
// @lc code=end

