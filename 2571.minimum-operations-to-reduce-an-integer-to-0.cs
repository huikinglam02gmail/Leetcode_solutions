/*
 * @lc app=leetcode id=2571 lang=csharp
 *
 * [2571] Minimum Operations to Reduce an Integer to 0
 */

// @lc code=start
public class Solution 
{
    /// <summary>Gets the number of bits needed to represent the number.</summary>
    public int Size(int bits)
    {
        var size = 0;
        while(bits != 0)
        {
            bits >>= 1;
            size++;
        }
        return size;
    }

    public static int SparseBitcount(int n)
    {
        int count = 0;
        while (n != 0)
        {
            count++;
            n &= (n - 1);
        }
        return count;
    }
    public int MinOperations(int n) 
    {
        int l = Size(n);
        int result = 0;
        for (int i = 0; i <= l; i++)
        {
            if ((n & (1 << i)) != 0)
            {
                if (SparseBitcount(n + (1 << i)) < SparseBitcount(n))
                {
                    n += (1 << i);
                }
                result++;
            }
        }
        return result;
    }
}
// @lc code=end

