/*
 * @lc app=leetcode id=2215 lang=csharp
 *
 * [2215] Find the Difference of Two Arrays
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
public class Solution 
{
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) 
    {
        List<IList<int>> result = new List<IList<int>>();
        for (int i = 0; i < 2; i++)
        {
            HashSet<int> nums1Set = new HashSet<int>(nums1);
            HashSet<int> nums2Set = new HashSet<int>(nums2);
            if (i == 0)
            {
                nums1Set.ExceptWith(nums2Set);
                result.Add(nums1Set.ToList());
            }
            else
            {
                nums2Set.ExceptWith(nums1Set);
                result.Add(nums2Set.ToList());
            }
        }
        return result;
    }
}
// @lc code=end

