/*
 * @lc app=leetcode id=1546 lang=csharp
 *
 * [1546] Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
 */

// @lc code=start
public class Solution 
{
    public int MaxNonOverlapping(int[] nums, int target) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        int prefix = 0;
        int n = nums.Length;
        int[] counts = new int[n];

        hashTable.Add(prefix, -1);
        Array.Fill(counts, 0);

        for (int i = 0; i < n; i++)
        {
            prefix += nums[i];
            if (i > 0)
            {
                counts[i] = counts[i-1];
            }
            if (hashTable.ContainsKey(prefix - target))
            {
                if (hashTable[prefix - target] >= 0)
                {
                    counts[i] = Math.Max(counts[i], counts[hashTable[prefix - target]] + 1);
                }
                else
                {
                    counts[i] = Math.Max(counts[i], 1);
                }
                
            }
            hashTable[prefix] = i;
        }
        return counts[n-1];
    }
}
// @lc code=end

