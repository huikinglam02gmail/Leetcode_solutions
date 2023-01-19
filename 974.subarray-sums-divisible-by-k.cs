/*
 * @lc app=leetcode id=974 lang=csharp
 *
 * [974] Subarray Sums Divisible by K
 */

// @lc code=start
public class Solution 
{
    public int mod(int num, int divisor)
    {
        while (num < 0)
        {
            num += divisor;
        }
        return num % divisor;
    }

    public int SubarraysDivByK(int[] nums, int k) 
    {
        int prefix = 0;
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        hashTable.Add(prefix, 1);
        foreach (int num in nums)
        {
            prefix = mod(num + prefix, k);
            if (!hashTable.ContainsKey(prefix))
            {
                hashTable.Add(prefix, 0);
            }
            hashTable[prefix]++;
        }    
        int result = 0;
        foreach (int value in hashTable.Values)
        {
            result += value * (value - 1) / 2;
        }
        return result;
    }
}
// @lc code=end

