/*
 * @lc app=leetcode id=1726 lang=csharp
 *
 * [1726] Tuple with Same Product
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int TupleSameProduct(int[] nums) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        int n = nums.Length;

        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int product = nums[i] * nums[j];
                if (!hashTable.ContainsKey(product))
                {
                    hashTable[product] = 0;
                }
                hashTable[product]++;
            }
        }

        int result = 0;
        foreach (int v in hashTable.Values)
        {
            result += 4 * v * (v - 1);
        }

        return result;    
    }
}
// @lc code=end

