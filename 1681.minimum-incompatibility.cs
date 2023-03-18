/*
 * @lc app=leetcode id=1681 lang=csharp
 *
 * [1681] Minimum Incompatibility
 */

// @lc code=start
using System.Linq;
using System;
using System.Collections;
public class Solution 
{
    int[] Nums;
    List<int>[] current;

    public int backTrack(int i, int cand, int ans)
    {
        if (cand > ans)
        {
            return ans;
        }
        else if (i == Nums.Length)
        {
            return cand;
        }
        else
        {
            for (int j = 0; j < current.Length; j++)
            {
                int currentJLength = current[j].Count;
                if (currentJLength < (Nums.Length / current.Length + 1) && (currentJLength == 0 || Nums[i] > current[j].Last()) && (j == 0 || !current[j].SequenceEqual(current[j - 1])))
                {
                    current[j].Add(Nums[i]);
                    if (currentJLength == 0)
                    {
                        current[j].Add(Nums[i]);
                    }
                    ans = backTrack(i + 1, cand + current[j][current[j].Count - 1] - current[j][current[j].Count - 2], ans);
                    current[j].RemoveAt(current[j].Count - 1);
                    if (currentJLength == 0)
                    {
                        current[j].RemoveAt(current[j].Count - 1);
                    }                    
                }
            }
            return ans;
        }
    }

    public int MinimumIncompatibility(int[] nums, int k) 
    {
        Nums = nums.OrderBy(x => x).ToArray();
        current = new List<int>[k];
        current = current.Select(x => new List<int>()).ToArray();
        int result = backTrack(0, 0, Int32.MaxValue);
        if (result == Int32.MaxValue)
        {
            return -1;
        }
        else
        {
            return result;
        }
    }
}
// @lc code=end

