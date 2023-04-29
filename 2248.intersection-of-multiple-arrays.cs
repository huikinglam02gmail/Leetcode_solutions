/*
 * @lc app=leetcode id=2248 lang=csharp
 *
 * [2248] Intersection of Multiple Arrays
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public IList<int> Intersection(int[][] nums) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        foreach (int[] arr in nums)
        {
            foreach (int num in arr)
            {
                if (!hashTable.ContainsKey(num))
                {
                    hashTable.Add(num, 0);
                }
                hashTable[num]++;
            }
        }
        return hashTable.Where(kvp => kvp.Value == nums.Length).Select(kvp => kvp.Key).OrderBy(x => x).ToList();
    }
}
// @lc code=end

