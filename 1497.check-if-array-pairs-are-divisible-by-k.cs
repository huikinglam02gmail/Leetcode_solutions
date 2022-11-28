/*
 * @lc app=leetcode id=1497 lang=csharp
 *
 * [1497] Check If Array Pairs Are Divisible by k
 */

// @lc code=start
public class Solution 
{
    public bool CanArrange(int[] arr, int k) 
    {
        int[] modulo = new int[k];
        Array.Fill(modulo, 0);
        foreach (int num in arr)
        {
            modulo[(k + (num % k)) % k]++;
        }    
        if (modulo[0] % 2 != 0)
        {
            return false;
        }
        for (int i = 1; i < k / 2 + 1; i++)
        {
            if (i == k - i && modulo[i] % 2 != 0)
            {
                return false;
            }
            else if (i != k - i && modulo[i] != modulo[k-i])
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

