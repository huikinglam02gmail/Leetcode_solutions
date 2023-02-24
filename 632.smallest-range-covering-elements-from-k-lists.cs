/*
 * @lc app=leetcode id=632 lang=csharp
 *
 * [632] Smallest Range Covering Elements from K Lists
 */

// @lc code=start
using System;
using System.Collections.Generic;
public class Solution 
{
    public int[] SmallestRange(IList<IList<int>> nums) 
    {
        int globalMax = 100000;
        int globalMin = - 100000;
        int maxSoFar = - 100000;  
        PriorityQueue<int[], int> pq = new PriorityQueue<int[], int>();

        for (int i = 0; i <  nums.Count; i++)
        {
            globalMax = Math.Max(globalMax, nums[i][nums[i].Count - 1]);
            globalMin = Math.Min(globalMin, nums[i][0]);
            pq.Enqueue(new int[2]{i, 0}, nums[i][0]);
            maxSoFar = Math.Max(maxSoFar, nums[i][0]);
        }   

        int[] result = new int[2]{globalMin, globalMax};
        int diff = globalMax - globalMin;

        while(pq.TryDequeue(out int[] node, out int num))
        {
            if (maxSoFar - num < diff)
            {
                diff = maxSoFar - num;
                result[0] = num;
                result[1] = maxSoFar;
            }
            if (node[1] < nums[node[0]].Count - 1)
            {
                pq.Enqueue(new int[2]{node[0], node[1] + 1}, nums[node[0]][node[1] + 1]);
                maxSoFar = Math.Max(maxSoFar, nums[node[0]][node[1] + 1]);
            }
            else
            {
                break;
            }
        }
        return result;
    }
}
// @lc code=end

