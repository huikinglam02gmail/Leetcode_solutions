/*
 * @lc app=leetcode id=912 lang=csharp
 *
 * [912] Sort an Array
 */

// @lc code=start
using System.Collections.Generic;
public class Solution
{
    public int[] SortArray(int[] nums) 
    {
        PriorityQueue<int, int> queue = new PriorityQueue<int, int>();
        foreach(int num in nums)
        {
            queue.Enqueue(num, num);
        }
        List<int> result = new List<int>();
        while (queue.TryDequeue(out int num, out int P))
        {
            result.Add(num);
        } 
        return result.ToArray();
    }
}
// @lc code=end

